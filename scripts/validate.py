"""Offline public-source checks plus ESPHome validation in an isolated fixture tree."""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

import jinja2
import yaml

ROOT = Path(__file__).resolve().parents[1]


class Loader(yaml.SafeLoader):
    pass


# These tags are resolved by ESPHome itself below; this pass checks YAML shape.
Loader.add_multi_constructor("!", lambda loader, tag, node: loader.construct_scalar(node))


def check_source():
    public = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT, text=True,
    ).splitlines()
    for name in public:
        p = ROOT / name
        assert not (p.name == "secrets.yaml" or p.name.endswith(".local.yaml")), name
        assert not any(part in ("private", "captures", ".esphome") for part in p.parts), name
        if p.suffix in (".yaml", ".yml"):
            data = yaml.load(p.read_text(), Loader=Loader)
            assert data is not None, name
            text = p.read_text()
            # Public RF fixtures must remain empty and gated off.
            for value in re.findall(r'^\s*rf_enabled:\s*(.+)$', text, re.M):
                assert value.strip("\"' ") == "false", (name, "enabled RF")
            for value in re.findall(r'^\s*rf_pulses:\s*(.+)$', text, re.M):
                assert value.strip("\"' ") == "0", (name, "RF access pattern")
        if p.suffix == ".md":
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', p.read_text()):
                if "://" in target or target.startswith(("#", "mailto:")):
                    continue
                assert (p.parent / target.split("#")[0]).exists(), (name, target)
    ET.parse(ROOT / "assets/wiring.svg")
    print(f"Public paths, YAML syntax, local Markdown links and SVG checked ({len(public)} files)")


def check_cover():
    config = yaml.safe_load((ROOT / "home-assistant/garage-cover.yaml").read_text())
    cover = config["template"][1]["cover"][0]
    request = config["script"]["garagewave_request"]
    assert request["mode"] == "single"
    assert request["sequence"][-1] == {"delay": "00:00:30"}
    assert "stop_cover" not in cover
    env = jinja2.Environment(undefined=jinja2.StrictUndefined)
    env.filters["bool"] = lambda value: value in (True, "true", "on", 1)
    guard = env.from_string(request["sequence"][0]["value_template"])
    available = env.from_string(cover["availability"])
    sensor = "binary_sensor.garagewave_door_open"
    button = "button.garagewave_transmit"
    connectivity = "binary_sensor.garagewave_connectivity"
    checks = 0
    for state in ("on", "off", "unknown", "unavailable"):
        for connected in ("on", "off", "unavailable"):
            for button_state in ("unknown", "unavailable", "2026-10-29T12:00:00Z", None):
                for target in (True, False):
                    values = {sensor: state, connectivity: connected}
                    if button_state is not None:
                        values[button] = button_state
                    context = dict(
                        states=lambda entity: values.get(entity, "unknown"),
                        is_state=lambda entity, value: values.get(entity) == value,
                        expand=lambda entity: [entity] if entity in values else [],
                        target_open=target,
                    )
                    ready = state in ("on", "off") and connected == "on" and button_state not in (None, "unavailable")
                    expected = ready and ((state == "off" and target) or (state == "on" and not target))
                    assert (guard.render(**context).strip() == "True") == expected, context
                    assert (available.render(**context).strip() == "True") == ready
                    checks += 1
    print(f"Home Assistant availability/direction guard: {checks} combinations passed")


def check_esphome(compile_firmware=False):
    with tempfile.TemporaryDirectory(prefix="garagewave-validation-") as tmp:
        tree = Path(tmp) / "esphome"
        shutil.copytree(ROOT / "esphome", tree,
                        ignore=shutil.ignore_patterns(".esphome", "secrets.yaml", "*.local.yaml", "private"))
        for folder in (tree, tree / "examples"):
            shutil.copyfile(tree / "examples/secrets.example.yaml", folder / "secrets.yaml")
        examples = [tree / "garagewave-stamp-s3a.yaml",
                    tree / "examples/garage-fixed-code.example.yaml",
                    tree / "examples/receiver-debug.example.yaml"]
        for example in examples:
            subprocess.run(["esphome", "config", str(example)], check=True, stdout=subprocess.DEVNULL)
        if compile_firmware:
            for example in examples[1:]:
                subprocess.run(["esphome", "compile", str(example)], check=True)
    print("ESPHome examples validated using public dummy credentials; local files untouched")


if __name__ == "__main__":
    check_source()
    check_cover()
    check_esphome("--compile" in sys.argv)

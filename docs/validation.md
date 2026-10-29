# Validation matrix

GarageWave works on my legacy Stanley fixed-code opener. I haven't established
compatibility with other opener types yet.

The public examples keep my garage signal out of Git. They pass the software
checks below, but you'll need to test your own configured build on your hardware.
The detailed hardware checks are listed separately so a working installation
isn't confused with a complete test of every feature and failure case.

| Layer | Result |
|---|---|
| Public YAML syntax and local Markdown links | Passed |
| ESPHome configuration: root, garage example, receiver example | Passed |
| ESP-IDF ESP32-S3 firmware compilation | Both garage and receiver examples passed (ESPHome 2026.10.1, ESP-IDF 5.5.6) |
| Home Assistant template request/availability logic | 96 availability/direction combinations passed |
| Home Assistant full config check | Passed isolated Home Assistant 2026.10.4 check for cover package and automations; live instance untouched |
| ESP32 boot / USB / Wi-Fi / encrypted API / OTA | Not separately checked with the public examples |
| CC1101 SPI initialization | Not separately checked with the public examples |
| RF reception | Optional debug example; not separately checked |
| RF transmission / waveform / frequency / modulation | My installation controls the door; no published RF measurements or private waveform |
| Stanley opener response | Working on my installation; other models not tested |
| Tilt pairing / polarity / feedback | Check the actual entity and polarity on your installation |
| Home Assistant supervised state-aware control | Not separately checked with the public examples |
| Disconnect / recovery / no replay / motion lockout | Not separately checked with the public examples |
| Regulatory compliance | Not established |
| Gitleaks 8.30.0 on staged public source | Passed; no findings |

## Repeat software checks

```sh
uv venv .venv
uv pip install --python .venv/bin/python esphome==2026.10.1
PATH="$PWD/.venv/bin:$PATH" python3 scripts/validate.py
# Optional full builds for both examples; no upload or radio operation:
PATH="$PWD/.venv/bin:$PATH" python3 scripts/validate.py --compile
```

The script copies public examples to a temporary tree, creates dummy `secrets.yaml`
fixtures there, and validates actual includes with ESPHome. It never overwrites
user credentials. The public fixture key is deliberately public, not a deployment
credential. RF remains disabled and the pulse list contains no control waveform.
CI checks local Markdown targets, SVG XML, public file policy, YAML and actual
Home Assistant Jinja availability/direction guards, then compiles both examples.
A credential scanner also checks Git history. No scanner can prove that every
possible embedded RF access credential is absent; review staged changes manually.

The Home Assistant logic check renders the actual source templates across normal,
unknown, unavailable, missing-button and connectivity states. It does not emulate
HA services, Zigbee, script scheduling, device timing or physical travel. Use HA's
configuration check and supervised acceptance tests before enabling live RF.

## Check your installation

Record date, exact board/module and antenna, firmware commit, frequency,
modulation, RF measurement method, travel time and results for the hardware checks.
Keep waveforms, access codes, personal entity inventories and screenshots private.
Verify that duplicate requests are dropped, a satisfied direction sends nothing,
unknown/offline states block commands, and restoring power/network/sensor causes
no replay. Test both directions with safety sensors working and the garage in sight.

The Home Assistant check also runs in CI using Python 3.14 and Home Assistant
2026.10.4, with a temporary configuration containing only the example package
and automations. No live installation is contacted. Both firmware builds produced
factory and OTA images in disposable build storage; none are published or flashed.

# Sharing and release preparation

The reusable packages use ESPHome's official
[packages](https://esphome.io/components/packages/) and
[substitutions](https://esphome.io/components/substitutions/) mechanisms.
Credential references remain in the user-local root file. After the files are
published, users can replace local package includes with immutable commit
references or a published tag. For example, **only after a real v1.0.0 tag exists**:

```yaml
packages:
  device: github://recalde/garagewave/esphome/packages/device.yaml@v1.0.0
  radio: github://recalde/garagewave/esphome/packages/radio-cc1101.yaml@v1.0.0
  garage: github://recalde/garagewave/esphome/packages/garage-button.yaml@v1.0.0
```

These are actual package paths, but **v1.0.0 has not been created**. Until publication
use the tested local includes; no remote import can fetch unpublished files.
Keep the root Wi-Fi/API/OTA blocks from the local example and override substitutions
there. Pin a reviewed published commit instead of following a moving branch.

`esphome.project` is present as `recalde.garagewave`, version `0.1.0-dev`.
Following the official [creator guidance](https://esphome.io/guides/creators/),
`dashboard_import` and `name_add_mac_suffix` were evaluated. We do not provide a
pre-flashed adoption image: private credentials, hardware matching and RF setup
still need deliberate local configuration. A MAC suffix is optional for multiple
units but changes entity names; explicit node names are clearer for this build.
USB flashing through Device Builder or CLI is the supported route. Browser-based
installation and one-click adoption are not advertised or hosted.

## Repository metadata to apply when publication is authorized

Description: An inexpensive, local-first ESPHome radio controller for compatible
fixed-code garage doors and other sub-GHz devices.

Topics: `esphome`, `home-assistant`, `esp32`, `cc1101`, `rf`, `garage-door`,
`zigbee`, `iot`, `sub-ghz`.

Source publication is separate from creating a version tag or GitHub release.
Review the [test matrix](validation.md), verify the exact module and sensor models,
and audit for credentials and RF codes before publication. A source-only preview
may accurately declare hardware untested; a working-garage release requires actual
RF, opener, sensor, disconnect/recovery and supervised cover evidence.

## Suggested first release description

GarageWave 0.1.0 preview introduces a small native ESPHome CC1101 configuration,
M5Stamp-S3A reference wiring, a momentary transmit button with duplicate suppression,
and a Home Assistant cover combining toggle commands with independent Zigbee tilt
feedback. Includes installation, compatibility, safety and troubleshooting guides,
a logical wiring SVG, validation fixtures and CI.

Transmission is disabled by default and no real garage signal is included.
The original repository was empty. Software validation does not establish RF or
physical operation; the owned 433 MHz board is not verified for the target 310 MHz
Stanley opener. See the dated test matrix for actual validation results. This is
an experimental source preview, not a verified hardware kit or rolling-code product.

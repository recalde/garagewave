# Sharing and release preparation

The reusable packages use ESPHome's official
[packages](https://esphome.io/components/packages/) and
[substitutions](https://esphome.io/components/substitutions/) mechanisms.
Credential references remain in the user-local root file. You can replace local package includes with an immutable commit
reference or a published tag. For example, **only after a real v1.0.0 tag exists**:

```yaml
packages:
  device: github://recalde/garagewave/esphome/packages/device.yaml@v1.0.0
  radio: github://recalde/garagewave/esphome/packages/radio-cc1101.yaml@v1.0.0
  garage: github://recalde/garagewave/esphome/packages/garage-button.yaml@v1.0.0
```

These are actual package paths, but **v1.0.0 has not been created**. Use the local includes or a commit that exists on GitHub until a tag is published.
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

## Repository metadata

Description: An inexpensive, local-first ESPHome radio controller for compatible
fixed-code garage doors and other sub-GHz devices.

Topics: `esphome`, `home-assistant`, `esp32`, `cc1101`, `rf`, `garage-door`,
`zigbee`, `iot`, `sub-ghz`.

Before tagging a release, run the [checks](validation.md), review the changes for
credentials and garage signals, and document any new hardware you've tested.
Keep specific compatibility claims tied to the hardware you've actually used.

## Suggested first release description

GarageWave 0.1.0 preview introduces a small native ESPHome CC1101 configuration,
M5Stamp-S3A reference wiring, a momentary transmit button with duplicate suppression,
and a Home Assistant cover combining toggle commands with independent Zigbee tilt
feedback. Includes installation, compatibility, safety and troubleshooting guides,
a logical wiring SVG, validation fixtures and CI.

I use GarageWave on my legacy Stanley fixed-code garage. This release shares the
ESPHome packages, wiring and Home Assistant setup so you can build your own.
Transmission starts disabled; add your own private remote signal before use.
Other compatible fixed-code devices can use the same approach with their own
radio settings and waveform. Rolling-code systems are not supported.
See the test matrix for software checks and remaining hardware checks.

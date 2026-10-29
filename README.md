# GarageWave

**Two chips. Eight jumper wires. One smart garage door.**

GarageWave is basically an ESP32, a CC1101 radio, and eight jumper wires.
That can be enough to bring an old fixed-code garage door into Home Assistant.
The hard part is knowing which radio, frequency, and configuration to use.
The clever software is already in ESPHome and Home Assistant; this project
puts the wiring, reusable configuration and independent door feedback together.
No cloud subscription, no new platform, no surgery inside the opener.

**Working installation: a legacy Stanley fixed-code garage door.**
GarageWave is in use on the maintainer's Stanley garage. The current garage
profile is built around that opener type; compatibility with every Stanley model
or other garage brand is not implied.

The same small ESPHome setup can be extended to other compatible fixed-code
openers and RF devices by adapting the radio settings and transmit signal.
Match the hardware, frequency, modulation and timing to your device; changing the
frequency alone is not enough. Rolling-code systems need a different approach.
See [protocols and extension ideas](docs/rf-protocols.md).

The public examples keep transmission disabled and omit the private garage access
signal. Configure your own credentials and authorized remote signal before use.
The maintainer's working installation is owner-reported; the published examples
have passed software checks but have not been independently tested on the garage.
See the [test matrix](docs/validation.md) for the distinction.

**Check the radio before buying:** the Stanley setup targets approximately
310 MHz. A module advertised for 433 MHz is not automatically suitable, even if
its CC1101 chip can tune to 310 MHz. Confirm the exact module variant and antenna
for your build. [Hardware, product links and cost](docs/hardware.md).

You need an M5Stamp-S3A (ESP32-S3, 8 MB flash), a frequency-appropriate CC1101
module and antenna, a mini breadboard, eight jumpers and USB power/programming.
A Third Reality Zigbee tilt sensor provides independent feedback through your
existing Home Assistant/Zigbee installation. The supplied controller and CC1101 module prices total **$16.49**, before the
antenna, breadboard, wires and power. See the BOM for price dates, product variants
and compatibility details.

![Owner-provided GarageWave assembly on a mini breadboard with jumper wiring and an external antenna](assets/assembly.png)

*The GarageWave assembly: a small breadboard, jumper wiring, USB cable and an
external antenna. Use the wiring map below and your exact module markings when
reproducing the build; some connections are obscured in the photo.*

![Reference electrical connections, not physical module orientation](assets/wiring.svg)

| CC1101 reference pin | M5Stamp-S3A |
|---|---|
| 1 GND | GND |
| 2 VCC | 3V3 |
| 3 GDO0 (TX) | GPIO15 |
| 4 CSN | GPIO5 |
| 5 SCK | GPIO9 |
| 6 MOSI | GPIO7 |
| 7 MISO | GPIO1 |
| 8 GDO2 (optional RX) | GPIO13 |

Use 3.3 V radio power and signaling, never 5 V. Verify the exact module's pin
numbers, orientation and markings before applying power; this is not a universal
physical pinout. [Wiring details](docs/wiring.md).

## Start here

1. Check module, antenna, remote frequency and fixed-code compatibility.
2. Wire with power disconnected and attach the correct antenna.
3. Install ESPHome **2026.10.1**, clone/download this project, and follow
   [getting started](docs/getting-started.md) to configure private credentials.
4. Flash over USB with transmission disabled; check Wi-Fi, API and SPI logs.
5. Identify your own authorized remote's signal, configure it only in an ignored
   local file, and perform a supervised RF test. No Stanley waveform is included.
6. Pair the independent tilt sensor; observe its actual open/closed polarity.
7. Install the [Home Assistant package](home-assistant/garage-cover.yaml), replace
   entity IDs, and test the cover with the physical garage in sight.

ESPHome exposes **GarageWave Transmit**, a momentary button backed by one shared
script. Home Assistant combines it with the sensor to request open only from
closed and close only from open. Unknown sensor state and offline transmission
block cover requests. A 30-second lockout drops duplicates rather than queueing
them; measure travel time and adjust it. A tilt sensor cannot establish precise
position, obstruction or whether the door is still moving. There is no stop action
or automatic retry. [Integration and behavior](docs/garage-door-integration.md).

## Documentation

- [Installation and private RF customization](docs/getting-started.md)
- [Hardware, bill of materials and compatibility](docs/hardware.md)
- [Wiring](docs/wiring.md)
- [Home Assistant and sensor setup](docs/garage-door-integration.md)
- [Protocols and other RF applications](docs/rf-protocols.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Security, physical safety and RF rules](docs/security-and-safety.md)
- [Validation and remaining tests](docs/validation.md)
- [Sharing, contributing and release preparation](docs/releasing.md)

## Safety and security

Use only equipment you own or are authorized to control. Fixed-code remotes are
replayable; ESPHome does not fix that. Keep actual RF codes, captures, DIP settings
and credentials private. Do not expose the controller directly to the internet;
use authenticated Home Assistant access and encrypted ESPHome API connections.
Never disable safety beams or obstruction detection. Transmission does not prove
movement; do not retry a command automatically. Exercise caution with unattended
closing. Respect local RF rules, including applicable U.S. FCC Part 15 requirements
such as [47 CFR §15.231](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-15/subpart-C/section-15.231).
A configured frequency, power or cooldown alone does not establish compliance.
This hobby project comes without warranty; verify suitability for your equipment.

## Contributing

Small documentation fixes and reproducible compatibility reports are welcome.
Include module markings, antenna, ESPHome version and exactly what you tested.
Remove credentials and access waveforms from logs and screenshots. Run the checks
in [validation](docs/validation.md) before sending a change. MIT licensed; built
on [ESPHome](https://esphome.io/) and [Home Assistant](https://www.home-assistant.io/).
Their software, documentation and trademarks belong to their respective owners;
no custom radio driver or third-party source code is vendored here.

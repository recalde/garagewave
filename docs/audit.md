# Design notes

I built GarageWave around my legacy Stanley fixed-code opener. The useful part
is keeping the setup small: ESPHome handles the radio, Home Assistant handles the
door logic, and a separate tilt sensor supplies feedback.

The firmware uses ESPHome's native CC1101 component with `remote_transmitter`.
There is no custom radio driver to install or maintain. The reusable packages
separate the board, radio and garage button so another fixed-code device can use
the same hardware with different radio settings and a different signal.

The public examples leave the garage signal blank and transmission disabled.
Keep your own access code and credentials in local files. The
[setup guide](getting-started.md) explains where they go.

My [assembly photo](../assets/assembly.png) and the
[parts list](hardware.md) show the build. Some module markings are hidden by the
wiring and glue, so use the exact part's datasheet when reproducing it. Radio
matching and antenna choice still matter, even when the chip supports the desired
frequency. [Testing](validation.md) separates software checks from the checks to
make on your own installation.

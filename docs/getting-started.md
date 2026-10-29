# Install without sending a garage command

1. Read [hardware compatibility](hardware.md). Establish the original remote's
   frequency with its label/documentation and an authorized measurement if needed.
2. Disconnect power, follow [wiring](wiring.md), check pin orientation and attach
   the correct antenna. Do not use the owned 433 MHz module as a proven 310 MHz part.
3. Install ESPHome Device Builder with ESPHome **2026.10.1**. Keep this repository's
   `esphome/` tree together in its configuration storage. Conventional local USB
   flashing is the supported initial setup; no browser firmware service is hosted.
4. Copy `esphome/garagewave-stamp-s3a.yaml` to
   `esphome/garagewave.local.yaml`. Copy `esphome/examples/secrets.example.yaml`
   to `esphome/secrets.yaml`. Replace **every** fixture credential. Generate an API
   encryption key using `openssl rand -base64 32`; never use the public dummy key.
5. Add your node/friendly name substitutions at the top of the local file.
   Leave `rf_enabled: "false"`. Run:

   ```sh
   esphome config esphome/garagewave.local.yaml
   esphome run esphome/garagewave.local.yaml --device /dev/ttyACM0
   ```

   Select the actual USB port. Use a data cable, boot/download mode if required,
   and inspect USB permissions if the device cannot be opened. This command
   builds and flashes; only use it on the intended attached controller.
6. Check boot logs, Wi-Fi and CC1101 SPI initialization. Add the discovered
   ESPHome device in Home Assistant and provide the private API encryption key.
   Confirm Connectivity and diagnostics. Pressing Transmit should only log that
   transmission is disabled.
7. For optional reception, copy the receiver example to an ignored `.local.yaml`
   **in the examples directory**, with private `examples/secrets.yaml`. Its paths
   are relative; do not move it elsewhere without fixing includes. Receiver dumps
   can contain access credentials: keep logs/captures private. The example uses
   310 MHz and the supplied RX pin but neither RF hardware nor timing is verified.

## Configure your own fixed-code signal privately

There is no verified Stanley protocol or waveform in this repository. Do not
interpret the dummy `0` as a usable remote signal. Determine modulation, actual
frequency, mark/space timings, frame boundaries and repeat count from your own
remote in an authorized setup. Prefer a documented native `transmit_*` encoder
only after identifying a matching protocol; otherwise raw signed microseconds
(positive marks, negative spaces) fit this architecture. Never infer timing from
DIP-switch count alone. Keep the original transmitter working.

In your ignored root `.local.yaml`, add substitutions containing your own
`rf_frequency`, `rf_modulation`, `rf_output_power`, `rf_pulses` (comma-separated
signed integer microseconds), `rf_repeat` and `rf_repeat_gap`. Only after module,
antenna, waveform and legal operation have been checked, set `rf_enabled: "true"`.
There is intentionally no public example of an enabled household waveform.
Start at suitably low power in a controlled setup; -30 dBm is a conservative
software default, not a certified power recommendation. Set `command_cooldown`
longer than measured travel time plus a margin (default 30s), and match the HA
lockout. Keep total RF airtime within applicable limits. The cooldown is an
application safeguard, not proof of RF compliance.

Public packages contain no `!secret` references. Secrets and waveform
substitutions belong in the local entry configuration, so the same packages can
be imported remotely. An optional private include file should use `.local.yaml`
or live under `private/`. Never upload your local files to an issue or PR.

Revalidate, compile and perform exactly one supervised test with the garage in
sight and people/objects clear. Verify movement independently; never retry merely
because a command timed out. Then add the tilt sensor and
[Home Assistant cover](garage-door-integration.md). Hardware failures should be
investigated locally before enabling remote operation.

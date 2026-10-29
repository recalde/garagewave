# Security, physical safety and radio operation

Operate only equipment you own or are authorized to control. A replayable
fixed-code remote remains replayable after adding ESPHome. Keep DIP positions,
real RF patterns, captures, SSIDs/passwords, API encryption keys and OTA credentials
out of Git, issue text, CI artifacts, screenshots and debug logs. `.gitignore`
reduces accidents but is not a security boundary. Review staged changes and run
secret scanning before publication. Rotate/change exposed credentials or fixed
codes according to the equipment's supported procedure.

Use private Wi-Fi credentials, encrypted native ESPHome API and authenticated HA
access. Keep the device on a trusted network; no public forwarding to firmware
services. Transmit is a physical-access capability. Limit who can press it in HA.
Controller availability cannot confirm delivery to the radio or opener.

Never bypass safety beams or obstruction protection. A tilt sensor is not an
obstruction detector. Keep the original controls available. Test with the garage
in sight, maintain clearance, and take particular care with unattended closing.
Never infer movement from a successful API call and never automatically retry a
toggle after a failed or uncertain result. Unknown/offline state blocks reference
cover actions. Intermediate motion, stale Zigbee state and restarts need human
judgment; this is not a certified safety controller.

Follow local RF rules. In the U.S. consult
[FCC Part 15](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-15)
and applicable provisions of
[47 CFR §15.231](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-15/subpart-C/section-15.231).
These address control-signal operation, timing, emissions and other conditions;
a component's tunable range, low configured power, a 30-second application lockout,
or a module seller's claim does not establish compliance of the assembled device.
Verify the final hardware, antenna, frequency, airtime and emissions against the
rules that actually apply. No regulatory certification is claimed here.

MIT software is supplied without warranty. Evaluate hardware suitability and
local requirements before allowing it to move machinery.

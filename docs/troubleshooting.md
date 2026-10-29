# Troubleshooting

Start with RF disabled. Change one thing at a time, and do not retry door commands
automatically. See [validation](validation.md) for what has actually been checked.

| Symptom | Check |
|---|---|
| USB missing | Data-capable cable, actual carrier/connector, download mode, port permissions and power |
| Compile/schema failure | Pinned ESPHome 2026.10.1; read first error; retain include tree and generate private secrets |
| Version incompatible | Native CC1101 schema changes; use pinned version before trying newer versions |
| Wi-Fi/API unavailable | 2.4 GHz network, private SSID/password, routing and matching API key; never paste secrets into issues |
| SPI fails / FF0F / FFFF / 0000 | 3.3 V supply, ground, exact module orientation, CSN/MOSI/MISO/SCK continuity |
| No reception | Correct matched module/antenna/frequency, GDO2 pin, receiver debug logging, modulation and actual signal presence |
| No transmitted signal | `rf_enabled` is false by default; verify your private waveform, GDO0 wiring and TX/RX lifecycle |
| Remote doesn't respond | Actual measured frequency, antenna, modulation, signed pulse timing, frame repeats; a successful compile doesn't confirm the radio signal |
| 433 MHz board at 310 | Do not solve matching-network mismatch with more transmit power; obtain suitable hardware |
| Rolling-code remote | Unsupported; fixed replay is not an implementation of rolling-code authentication |
| Door state reversed | Observe fully closed/open, invert normalized sensor polarity only, recheck offline state |
| Tilt sensor offline | Battery, Zigbee mesh/coordinator, device model support; keep cover unavailable |
| HA cover/button missing | Actual entity IDs, YAML package inclusion, Developer Tools config check, entity-name suffixes |
| Cover unavailable initially | Check the button exists and Connectivity is on; an unknown last-press timestamp alone does not block requests |
| Duplicate/unexpected activations | One shared script, single mode and both cooldowns; inspect other automations/physical remotes; measure travel time |
| Recovery sends a command | Stop testing; no boot/availability automation should press Transmit; never implement retries |

If pulse capture is necessary, use your own remote, keep dumps private, and remove
access data from any shared log. Module RF band and pin numbering must be checked
against the exact variant rather than a visually similar internet photograph.

# Initial reconnaissance — 2026-10-29

The public repository cloned successfully into the development workspace but contained no tracked
files and no commits. There was no YAML, driver, C++, Home Assistant configuration,
license, secret, compiled artifact, or physical-test evidence to inspect.
Consequently this implementation is a new reference configuration, not a migration
of a working Stanley transmitter. No actual protocol, modulation, pulse timings,
repeat settings or DIP-switch code can be inferred from the empty repository.

The owner's request supplies the wiring and owned hardware; neither was physically
inspected. Exact module markings and private prototype configuration
remain useful follow-up evidence. Do not publish a working waveform from them.
Native ESPHome CC1101 plus remote_transmitter covers the proposed asynchronous
OOK architecture without external components. OOK and 310 MHz are target settings,
not measured properties of this remote. See [validation](validation.md).

## Follow-up — assembly photo, 2026-10-29

The owner supplied the [assembly photo](../assets/assembly.png), now included in
the README. It shows the breadboard-mounted controller, jumper wiring, radio PCB
and connected external antenna. Obscured markings and connections prevent exact
part identification or end-to-end wiring verification. No new boot, SPI, RF,
opener or sensor test evidence was supplied.

## Follow-up — owner-provided product listings

The owner supplied an eifagur 315 MHz SMA male antenna two-pack listing
([B0GTTQBR39](https://www.amazon.com/dp/B0GTTQBR39)) and a CC1101 module listing
([B0D2TMTV5Z](https://www.amazon.com/dp/B0D2TMTV5Z)) with an $8.99 price. No
antenna price or purchase date accompanied these records. The module title lists
315/433/868/915 MHz, but the exact selected variant and hardware matching network
remain unresolved. Neither listing establishes 310 MHz operation or changes the
physical-test status. See the updated [BOM](hardware.md).

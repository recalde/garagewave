# Eight electrical connections

[The README pin table](../README.md) and [SVG diagram](../assets/wiring.svg)
match the owner-supplied reference. The diagram is a logical wiring map, not a
photograph, footprint, connector view or guarantee of module pin orientation.
Pin 1 must be located using the exact module datasheet and physical markings.
Do not infer pin numbering from which way an antenna connector points.

Disconnect power. Put the Stamp's 2.54 mm headers in a mini breadboard, ensuring
separate nets are not shorted in connected rows. Fit eight short jumpers as shown,
then check continuity and 3V3-to-GND resistance before power-up. Jumper connector
sex depends on the headers you actually fitted. GDO0 is the TX input; GDO2 is the
optional RX output. Both use 3.3 V signaling. Never connect radio VCC to 5 V.
The ESP board may accept USB power separately; that does not make radio VCC 5 V.

Attach the correctly matched antenna and ensure the module's power requirements
fit the board's 3.3 V regulator. Confirm module pin orientation before publishing
an assembly photograph or treating this table as validated hardware wiring.

For SPI errors, inspect CSN GPIO5, SCK GPIO9, MOSI GPIO7 and MISO GPIO1, common
ground and supply voltage first. `0000`, `FFFF` or `FF0F` identity readings can
indicate communication trouble. Check for swapped MOSI/MISO, loose breadboard
contacts and incorrect pin numbering before adjusting RF settings.

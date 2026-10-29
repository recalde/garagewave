# Eight jumper wires

This is how I wired my Stamp to the CC1101. The [pin table](../README.md) and
[diagram](../assets/wiring.svg) show the same eight connections.

The diagram shows electrical connections, not the physical header layout. Find
pin 1 using your module's markings and datasheet; don't judge orientation from
the antenna connector alone.

## Connect the boards

Disconnect power first. Put the Stamp's 2.54 mm headers in the mini breadboard,
then connect the eight Dupont wires using the pin table. Check which breadboard
holes share a connection so you don't accidentally short two pins together.

Use jumper ends that fit your headers, and keep the wires together as a ribbon
where practical. GDO0 carries the transmit signal; GDO2 is used for optional
reception. Both use 3.3 V signaling.

Power the radio from **3.3 V, never 5 V**, and connect both boards to the same
ground. USB can power the Stamp, but the radio still connects to its 3V3 pin.
Check your module's current requirements against the Stamp's regulator capacity.

Before switching on, check continuity, look for a short between 3V3 and GND, and
attach the correct antenna.

## If SPI isn't working

Check CSN GPIO5, SCK GPIO9, MOSI GPIO7 and MISO GPIO1, then the common ground and
supply voltage. Readings such as `0000`, `FFFF` or `FF0F` can point to a communication
problem. Look for swapped MOSI/MISO wires, loose breadboard contacts or a reversed
module connection before changing the radio settings.

# My hardware

I use this setup with my legacy Stanley fixed-code garage opener. The radio sends
the same toggle command as the remote, and a THIRDREALITY Zigbee tilt sensor tells
Home Assistant whether the door is open or closed.

## Parts used

| Part | Store | Price (USD) |
|---|---|---|
| M5StampS3A with 2.54 mm headers | M5Stack | $7.50 — already had it |
| CC1101 radio module with SMA connector | Amazon | $8.99 |
| eifagur 315 MHz SMA male antenna, two-pack (use one) | Amazon | $9.99 per pack |
| ELEGOO 170-point mini breadboards, six-pack (use one) | Amazon | $5.99 per pack |
| ELEGOO 120-piece Dupont ribbon wire kit (use eight wires) | Amazon | $6.98 per kit — already had it |
| USB cable and power supply | Already on hand | No additional cost |
| THIRDREALITY Zigbee Smart Garage Door Tilt Sensor | Amazon | Not available |

I use the THIRDREALITY sensor with adjustable sensitivity and advertised two-year
battery life. It needs a Zigbee hub or coordinator; mine connects to Home Assistant
separately from the ESP32. See [sensor setup](garage-door-integration.md).

## Cost

I already had the M5Stamp, USB power and a supply of Dupont wires. The radio,
antenna two-pack and breadboard six-pack total **$24.97**, before the tilt sensor.
That buys spare antennas and breadboards as well as the ones used here.

Buying the M5Stamp and wire kit too brings the listed parts total to **$39.45**,
excluding USB power and the tilt sensor. The sensor price isn't recorded, so a
complete total including door feedback is still unavailable. These totals use
whole-pack prices rather than dividing the cost among the parts used.

These are historical prices, before shipping and tax. An existing Home Assistant
installation and Zigbee coordinator are also needed and aren't included here.

## Before buying

My Stanley setup targets approximately 310 MHz. Check the exact radio variant
and antenna for your opener: a module sold for 433 MHz isn't automatically suitable
at 310 MHz, even if the CC1101 chip can tune there. My antenna is sold for 315 MHz;
I haven't measured its performance at 310 MHz.

Other fixed-code openers may use the same hardware with different settings and a
different signal. Match the frequency, modulation and protocol before transmitting.
Keep your own garage code private.

## Wiring tip

I recommend Dupont ribbon wires: peel off the eight wires you need and keep them
together as a ribbon to make the wiring easier to follow and less tangled. The
ELEGOO kit includes male-to-female, male-to-male and female-to-female wires; use
the ends that match your board and radio headers.

## Assembly

Here's [my build](../assets/assembly.png). The Stamp sits on a mini breadboard,
with jumper wires running to the radio and an external antenna on its SMA
connector. I use the Stamp's USB connection for power and programming.

Follow the [wiring table](wiring.md) and your module's pin markings. Use GPIO
numbers rather than header positions, and power the radio from **3.3 V, never 5 V**.

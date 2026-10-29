# My hardware

I use this setup with my legacy Stanley fixed-code garage opener. The radio sends
the same toggle command as the remote, and a THIRDREALITY Zigbee tilt sensor tells
Home Assistant whether the door is open or closed.

## Parts used

| Part | Store | Price (USD) |
|---|---|---|
| M5StampS3A with 2.54 mm headers | M5Stack | $7.50 — already had it |
| CC1101 radio module with SMA connector | Amazon | $8.99 |
| eifagur 315 MHz SMA male antenna, two-pack | Amazon | Not available |
| Mini breadboard | Not recorded | Not available |
| Eight jumper wires | Not recorded | Not available |
| USB cable and power supply | Already on hand | No additional cost |
| THIRDREALITY Zigbee Smart Garage Door Tilt Sensor | Amazon | Not available |

I use the THIRDREALITY sensor with adjustable sensitivity and advertised two-year
battery life. It needs a Zigbee hub or coordinator; mine connects to Home Assistant
separately from the ESP32. See [sensor setup](garage-door-integration.md).

## Cost

The parts are an ESP32 board, radio, antenna, breadboard, eight jumpers, USB power
and a separate tilt sensor. **The board and radio total $16.49.** I already had
the M5Stamp and USB power, so **the known additional cost is $8.99 for the radio**,
plus the antenna, breadboard, wires and tilt sensor. I don't have prices recorded
for those items, so I can't give a complete build total yet.

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

## Assembly

Here's [my build](../assets/assembly.png). The Stamp sits on a mini breadboard,
with jumper wires running to the radio and an external antenna on its SMA
connector. I use the Stamp's USB connection for power and programming.

Follow the [wiring table](wiring.md) and your module's pin markings. Use GPIO
numbers rather than header positions, and power the radio from **3.3 V, never 5 V**.

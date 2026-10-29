# Hardware, compatibility and cost

The reference controller uses the M5Stamp-S3A / ESP32-S3FN8 with 8 MB flash,
2.4 GHz Wi-Fi and 3.3 V GPIO on a mini breadboard with 2.54 mm headers.
Check whether your exact board/carrier provides a USB-C programming connection;
verify the connector and USB data wiring before buying a cable. The software
uses `esp32-s3-devkitc-1` with ESP-IDF as a compile target, not proof of identical
board wiring. Pin labels mean GPIO numbers, not header positions.

## Compatibility

My setup works with a legacy Stanley fixed-code opener at approximately 310 MHz.
These are the parts and limits to check when building your own:

| Part | What to check |
|---|---|
| M5StampS3A with 2.54 mm headers | Use the GPIO labels, not physical header positions |
| CC1101 module B0D2TMTV5Z | The listing names several bands; confirm the exact module variant and matching network |
| eifagur 315 MHz SMA male antenna, two-pack B0GTTQBR39 | Advertised for 315 MHz; performance at 310 MHz has not been measured here |
| E07-M1101D-style 433 MHz module | Its specified 387–464 MHz band does not establish suitability at 310 MHz |
| Stanley ten-position DIP remote | Configure your own fixed-code signal; my access code is not included |
| Third Reality 3RVS01031Z tilt sensor | Check model support, actual entity ID and open/closed polarity in your Zigbee setup |
| Other openers | Match hardware and protocol, then test; the current garage profile targets the Stanley setup |

The [TI chip specifications](https://www.ti.com/product/CC1101) describe three
separate bands, not every frequency between 300 and 928 MHz. The
[Ebyte module page](https://www.cdebyte.com/products/E07-M1101D-TH) specifies
387–464 MHz. Confirm your exact SMA/TH/other variant against its own datasheet.
A label saying “315 MHz” is not enough to declare adequate performance at 310 MHz.
Do not buy the linked 433 MHz example expecting a proven Stanley build.

## Bill of materials

The controller and radio prices below are what I paid, not current quotes. Other vendor listings were checked 2026-10-29. Shipping, tax,
tools and existing HA infrastructure are excluded. Store stock and prices vary. Budget allowances below are planning
estimates, not retrieved vendor quotes.

| Item | Quantity | Price / allowance | Link / notes |
|---|---|---|---|
| M5StampS3A with 2.54 mm header pins | 1 | $7.50, purchase price | [Exact M5Stack product/variant](https://shop.m5stack.com/products/m5stamps3a-with-2-54-header-pin?variant=46720097812737) |
| E07-M1101D-SMA **433 MHz illustration only** | 1 | $2.84 listed, out of stock | [Ebyte store](https://ebyteiot.com/products/ebyte-e07-m1101d-sma-cc1101-wireless-transceiver-module-low-power) |
| CC1101 module advertised as 315/433/868/915 MHz | 1 listing item; pack contents unconfirmed | $8.99, purchase price | [Amazon B0D2TMTV5Z](https://www.amazon.com/dp/B0D2TMTV5Z) |
| Suitable verified 310/315 MHz module | 1 | Pending exact variant and testing | The Amazon listing above is not yet a verified recommendation |
| eifagur 315 MHz SMA male antenna | 2-pack listing | Price not recorded | [Amazon B0GTTQBR39](https://www.amazon.com/dp/B0GTTQBR39) |
| Verified antenna near 310 MHz | 1 | Allow $3–10 | Estimate; listed 315 MHz antenna performance at 310 MHz unverified |
| Mini breadboard | 1 | Allow $3–6 | Estimate; [size example](https://www.adafruit.com/product/65) |
| Female-to-male jumpers | 8 | Allow $3–6 per pack | Estimate; [connector example](https://www.adafruit.com/product/1954) |
| USB-C data cable and suitable power supply/carrier | 1 | Allow $5–12 if not already owned | Estimate; confirm board connector |
| Case/mounting | optional | Allow $0–10 | Estimate |
| Third Reality tilt sensor | optional | $19.99 current garage-tilt listing | [Manufacturer](https://www.thirdreality.com/products/smart-garage-door-tilt-sensor) |

The controller and Amazon module cost **$16.49**, excluding the separately listed antenna,
breadboard, wires and power. This is a partial parts subtotal, not the cost of a
verified 310 MHz build; the antenna price and module variant remain unresolved.

The Amazon title's four frequency labels do not establish that one assembled
module is matched across all those bands. Confirm the purchased variant, actual
PCB markings, matching network and vendor documentation. The earlier E07-style
433 MHz identification remains provisional; the photo does not resolve it. The
eifagur antenna listing explicitly advertises 315 MHz-only suitability, not tested
310 MHz operation. Verify standard SMA connector mating (not RP-SMA), antenna
impedance and performance near the actual remote frequency before use. Product titles are useful for finding parts, but check the actual specifications.

The current tilt listing may describe a newer model: verify **3RVS01031Z** on the
actual device and the integration's model support; the price is not a guaranteed
quote for that exact model. The two-module 433 MHz price illustration is $10.34.
With estimated antenna, breadboard, wires and USB power, that illustration totals
about **$24–45** before optional case, or **$44–65** with a $19.99 tilt sensor.
A reliable all-in **310 MHz** cost remains pending the matched module and antenna.
Existing Home Assistant and a compatible Zigbee coordinator are additional
infrastructure, not included in these component totals.

## Assembly

Here's [my build](../assets/assembly.png): the Stamp sits on a mini breadboard,
with jumper wires running to the radio and an external antenna attached to its
SMA connector. The glue holds the connections in place but hides some labels.
Follow the [wiring table](wiring.md) and your module's pin markings when building
yours rather than trying to trace every wire in the photo.

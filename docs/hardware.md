# Hardware, compatibility and cost

The reference controller uses the M5Stamp-S3A / ESP32-S3FN8 with 8 MB flash,
2.4 GHz Wi-Fi and 3.3 V GPIO on a mini breadboard with 2.54 mm headers.
Check whether your exact board/carrier provides a USB-C programming connection;
verify the connector and USB data wiring before buying a cable. The software
uses `esp32-s3-devkitc-1` with ESP-IDF as a compile target, not proof of identical
board wiring. Pin labels mean GPIO numbers, not header positions.

| Item | Evidence / status | 310 MHz conclusion |
|---|---|---|
| M5StampS3A with 2.54 mm header pins | Header-equipped product variant identified; assembly photographed | Board boot and GPIO behavior untested |
| E07-M1101D-style 433 MHz CC1101 | Owner-reported model; radio PCB photographed, exact markings obscured | Outside manufacturer module band; not verified/supported at 310 |
| CC1101 silicon | TI specifies 300–348, 387–464, 779–928 MHz | Chip capability alone is insufficient |
| 315 MHz matched CC1101 module | Candidate; no exact tested SKU yet | Require vendor evidence and RF tests at 310 |
| eifagur 315 MHz SMA male antenna, two-pack (B0GTTQBR39) | Owner-provided listing; advertised for 315 MHz only | Performance at 310 MHz and identity of pictured antenna unverified |
| CC1101 module listing B0D2TMTV5Z | Owner-provided listing titled “315/433/868/915MHZ”; exact purchased variant/matching network unresolved | Listing title does not establish a 310 MHz-capable module |
| Stanley ten-position DIP remote | Owner-reported legacy fixed code, approximately 310 MHz | Exact frequency, modulation, timing and repeats unknown |
| Third Reality 3RVS01031Z tilt sensor | Requested reference model; not inspected | Pairing, exposed entity and polarity untested |
| Full controller + garage | Assembly photo supplied; no operating-test evidence | No tested operation claimed |

The [TI chip specifications](https://www.ti.com/product/CC1101) describe three
separate bands, not every frequency between 300 and 928 MHz. The
[Ebyte module page](https://www.cdebyte.com/products/E07-M1101D-TH) specifies
387–464 MHz. Confirm your exact SMA/TH/other variant against its own datasheet.
A label saying “315 MHz” is not enough to declare adequate performance at 310 MHz.
Do not buy the linked 433 MHz example expecting a proven Stanley build.

## Bill of materials

USD prices: the controller and Amazon module prices are supplied historical
prices, not current quotes. Other vendor listings were checked 2026-10-29. Shipping, tax,
tools and existing HA infrastructure are excluded. Store stock and prices vary. Budget allowances below are planning
estimates, not retrieved vendor quotes.

| Item | Quantity | Price / allowance | Evidence |
|---|---|---|---|
| M5StampS3A with 2.54 mm header pins | 1 | $7.50, supplied historical price | [Exact M5Stack product/variant](https://shop.m5stack.com/products/m5stamps3a-with-2-54-header-pin?variant=46720097812737) |
| E07-M1101D-SMA **433 MHz illustration only** | 1 | $2.84 listed, out of stock | [Ebyte store](https://ebyteiot.com/products/ebyte-e07-m1101d-sma-cc1101-wireless-transceiver-module-low-power) |
| CC1101 module advertised as 315/433/868/915 MHz | 1 listing item; pack contents unconfirmed | $8.99, owner-provided price; date unspecified | [Amazon B0D2TMTV5Z](https://www.amazon.com/dp/B0D2TMTV5Z) |
| Suitable verified 310/315 MHz module | 1 | Pending exact variant and testing | The Amazon listing above is not yet a verified recommendation |
| eifagur 315 MHz SMA male antenna | 2-pack listing | Price not supplied | [Amazon B0GTTQBR39](https://www.amazon.com/dp/B0GTTQBR39) |
| Verified antenna near 310 MHz | 1 | Allow $3–10 | Estimate; listed 315 MHz antenna performance at 310 MHz unverified |
| Mini breadboard | 1 | Allow $3–6 | Estimate; [size example](https://www.adafruit.com/product/65) |
| Female-to-male jumpers | 8 | Allow $3–6 per pack | Estimate; [connector example](https://www.adafruit.com/product/1954) |
| USB-C data cable and suitable power supply/carrier | 1 | Allow $5–12 if not already owned | Estimate; confirm board connector |
| Case/mounting | optional | Allow $0–10 | Estimate |
| Third Reality tilt sensor | optional | $19.99 current garage-tilt listing | [Manufacturer](https://www.thirdreality.com/products/smart-garage-door-tilt-sensor) |

The controller record identifies the header-equipped product variant; its historical
price does not establish current price or availability. The owner-supplied controller
and Amazon module prices total **$16.49**, excluding the separately listed antenna,
breadboard, wires and power. This is a partial parts subtotal, not the cost of a
verified 310 MHz build; the antenna price and module variant remain unresolved.

The Amazon title's four frequency labels do not establish that one assembled
module is matched across all those bands. Confirm the purchased variant, actual
PCB markings, matching network and vendor documentation. The earlier E07-style
433 MHz identification remains provisional; the photo does not resolve it. The
eifagur antenna listing explicitly advertises 315 MHz-only suitability, not tested
310 MHz operation. Verify standard SMA connector mating (not RP-SMA), antenna
impedance and performance near the actual remote frequency before use. These
listing details are owner-provided records, not independently verified specifications.

The current tilt listing may describe a newer model: verify **3RVS01031Z** on the
actual device and the integration's model support; the price is not a guaranteed
quote for that exact model. The two-module 433 MHz price illustration is $10.34.
With estimated antenna, breadboard, wires and USB power, that illustration totals
about **$24–45** before optional case, or **$44–65** with a $19.99 tilt sensor.
A reliable all-in **310 MHz** cost remains pending the matched module and antenna.
Existing Home Assistant and a compatible Zigbee coordinator are additional
infrastructure, not included in these component totals.

## Assembly photograph

The [owner-provided photo](../assets/assembly.png), supplied 2026-10-29, shows an
orange-covered controller on a yellow mini breadboard, jumper wiring, a connected
USB cable, and a separate blue radio PCB with an external antenna connector and
black antenna. Adhesive obscures some connections; the radio's identifying
markings and complete pin labels cannot be read. The photo documents the assembly
but cannot confirm every electrical connection, radio model, antenna tuning,
frequency, SPI initialization or successful garage operation. All operating-test
statuses above remain unchanged.

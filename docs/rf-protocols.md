# RF protocols and extension ideas

Frequency matching is necessary but insufficient: module matching, antenna,
modulation, encoding, pulse timing, repeats and protocol all matter. A ten-position
DIP switch does not identify a native ESPHome encoder. My working garage signal stays private. The public profile targets 310 MHz /
ASK-OOK, but you need to confirm the settings and waveform for your own remote.
Use timings from your own authorized remote rather than guessing them.

The reusable radio package uses SPI and native CC1101 asynchronous mode.
`remote_transmitter` drives GDO0 at 100% carrier duty for OOK baseband, with
`cc1101.begin_tx` before and `cc1101.begin_rx` after transmission. Optional
`remote_receiver` listens on GDO2. No custom driver or external component is needed.
The modulation substitution exposes native choices but changing it alone does not
create an interoperable FSK/packet application; review symbol rate, bandwidth,
packet handling and protocol separately.

| Idea | Direction | Additional work |
|---|---|---|
| Fixed-code outlets, simple switches, legacy remotes | TX | Identify authorized waveform; adapt application semantics |
| Compatible wireless doorbell | TX or RX | Identify protocol, never assume frequency means compatibility |
| Driveway/gate alerts | RX | Match sensor protocol; handle missing messages |
| Weather/environment sensors | RX | Decode a supported protocol; not automatically compatible |
| RF observation | RX | Authorized signals; keep access-code logs private |
| Personal telemetry | TX/RX | Separate packet protocol and legal airtime design |

A 433 MHz project can reuse the wiring and packages with an appropriately matched
433 MHz module/antenna and explicit frequency override, for example 433.92 MHz
only when that is the actual target. The owned board may be a candidate there;
it has not been tested here. Packet protocols require a different application
profile; this raw garage profile is not a generic packet modem. Proprietary,
encrypted and rolling-code systems are not supported by replaying a fixed waveform.
Do not bypass rolling-code security or record/control third-party access devices.

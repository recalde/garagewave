# Home Assistant knows the door state

The ESP32 transmits a momentary toggle and never assumes it succeeded. The tilt
sensor talks separately to Zigbee, not to an ESP GPIO or a firmware entity ID.
Use the official [Template integration](https://www.home-assistant.io/integrations/template/).

1. I use the THIRDREALITY Zigbee Smart Garage Door Tilt Sensor with adjustable
   sensitivity and advertised two-year battery life. Pair yours using ZHA or
   Zigbee2MQTT and the manufacturer's instructions. Check the model label and
   supported exposed entities.
   [Manufacturer firmware/support](https://www.thirdreality.com/pages/firmware/garage-door-tilt-sensor)
   covers both platforms; check the notes for your sensor's model and firmware.
2. Find the entity exposing door/contact state in Developer Tools → States.
   Observe and record its state with the garage fully closed and fully open.
   Do not assume `on` means open. Verify mounting, polarity and offline behavior.
3. Load `home-assistant/garage-cover.yaml` as a Home Assistant package:

   ```yaml
   homeassistant:
     packages:
       garagewave: !include garagewave/garage-cover.yaml
   ```

   Copy the supplied file under `/config/garagewave/garage-cover.yaml`. Merge with
   existing `homeassistant:` configuration rather than defining that key twice.
4. Replace `binary_sensor.garage_tilt`, `binary_sensor.garagewave_connectivity`
   and `button.garagewave_transmit` with actual
   entity IDs. The normalized template sensor assumes `on = open`; change its
   `state` template to check `off` if your observations prove reversed polarity.
   Leave its availability check accepting only `on` or `off`.
5. Check configuration in HA before reload/restart. Verify generated normalized
   sensor/cover entity IDs; existing names may cause numeric suffixes. Update all
   references, including dashboard and automation examples, to match.
6. Add the optional dashboard card. Merge optional automation examples under
   `automation:`; change entities/services as needed. They notify, never actuate.
7. With the garage in sight, confirm every row below. Disconnect the sensor and
   controller separately and verify requests are blocked. Restore them and check
   that no command is replayed. Do not simulate a sensor state while live RF is
   enabled unless the area is safe and you're intentionally testing movement.

| Observed door | Request | Expected command |
|---|---|---|
| Closed | Open | One toggle |
| Open | Open | None |
| Open | Close | One toggle |
| Closed | Close | None |
| Unknown / sensor unavailable | Either | None; cover unavailable |
| Transmitter unavailable | Either | None; cover unavailable |
| Within command lockout | Either | Dropped, no queue |

Both directions use the same RF signal. There are no independent open/close codes
or validated stop command. The cover reports the tilt sensor, not the last button
press. A button's state is its last-press timestamp and may be `unknown` before its first
press. The guard requires an existing button entity and explicit controller
connectivity rather than treating a missing timestamp as a disconnected device.

A single tilt sensor cannot measure precise travel, identify obstruction, guarantee
fresh state or distinguish every intermediate position. The 30-second shared HA
script lockout reduces repeat toggles while moving; measure full travel and
increase both HA and ESPHome delays as needed. It does not track motion or survive
HA restarts as a persistent interlock. Commands from physical remotes remain
outside this lockout. State changes during travel may happen well before travel
finishes. Test with supervision and keep opener safety mechanisms intact.

Optional examples cover left-open duration, overnight openings (a configurable
proxy for unexpected activity), low battery if exposed, and offline controller.
A recorded HA button press is not proof that the door moved, nor does battery
percentage prove sensor health. No last-command timestamp helper is implemented.

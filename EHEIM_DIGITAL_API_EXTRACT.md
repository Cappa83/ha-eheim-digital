# Eheim Digital API – Extrahierte Dokumentation

Quelle: https://api.eheimdigital.com/docs/category/eheim-digital-api

## Extraktions-Notizen
- Verwendete Befehle (Zusammenfassung):
  - `curl -sS https://api.eheimdigital.com/sitemap.xml`
  - `curl -sS https://api.eheimdigital.com/docs/category/eheim-digital-api/`
  - `python` (Skript zum Abruf aller `/docs/eheim_digital_api/`-Seiten und HTML-Parsing in Markdown)

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/autofeeder

# autofeeder+
The EHEIM autofeeder+ is a smart, WiFi-controlled feeding system for aquariums and terrariums. Using a smartphone, tablet, or PC/MAC, you can individually program feeding times and amounts, and set up fasting days. The device features overfeeding protection and sends email notifications when food levels are low. By synchronizing with other EHEIM WiFi devices, such as the thermocontrol+e heater or the professional 5e external filter, you can access additional features. The system provides feeding warnings when water temperature is too high, and filter speed can be adjusted during feeding times. Additional benefits include an actively ventilated food chamber (approx. 125 ml), operation with a safety power supply, a convenient cable length of 200 cm, and the ability to group devices together.

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/autofeeder-bio

# Set Daycycle mode
```
POST /autofeeder/bio
```
POST
### Set the Daycycle mode[​](#set-the-daycycle-mode)
In this mode, you can set up the feeding plan with up to four feedings per day.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/autofeeder-config

# Set Configuration
```
POST /autofeeder/config
```
POST
### Set the configuration[​](#set-the-configuration)
You can enable overfeeding protection and set up the sync partner filter to stop it while the feeding process is running. The overfeeding protection allows a maximum of 3 feedings per day to prevent unwanted events, such as the feeding process being triggered multiple times by the touch sensor.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/autofeeder-full

# Set autofeeder drum to full
```
POST /autofeeder/full
```
POST
### Resets the drum scale to full[​](#resets-the-drum-scale-to-full)
Only call the endpoint when you are sure that your drum is filled, in order to reset the level indicator to full.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/autofeeder-manual

# Feed once
```
POST /autofeeder/feed
```
POST
### Manual feeding[​](#manual-feeding)
To trigger a manual drum spin or feeding.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/autofeeder-status

# Get autofeeder+ status
```
GET /autofeeder
```
GET
### Reading the Current Status from the autofeeder+[​](#reading-the-current-status-from-the-autofeeder)
This API allows you to trigger a manual feeding and a reset of the drum scale.
#### Sync Partner Feature[​](#sync-partner-feature)
You can connect your filter as a sync partner. When feeding starts, the filter will adjust its relative speed for 10 minutes according to the predefined settings.
#### Configuration Structure[​](#configuration-structure)
The configuration is structured as follows:
- "configuration":[Monday, Thuesday, Whensday, ...., Sunday]
- "Monday":[[first Time, second Time][first Time drum spins, second time drum spins]]
```
  "configuration":[    [[180, 1200],[1, 2]],   #Monday    [[180, 1200],[2, 2]],   #Tuesday    [[],[]]                 #Wednesday (no feeding)    ......                  #All 7 days must be included, even if empty  ]
```
## Request[​](#request)
## Responses[​](#responses)
- 200

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/brightness-status-led

# Set status LED brightness
```
POST /brightness
```
POST
## Set status LED brightness level[​](#set-status-led-brightness-level)
The brightness level of the status LED allows users to adjust how bright the LED indicator lights up on the device. This setting can help improve visibility in various lighting conditions or reduce brightness to avoid distractions, providing flexibility for user preferences and environmental needs.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/changeauth

# Update credentials
```
POST /changeauth
```
POST
### Allows to update the login credentials username and password for the API.[​](#allows-to-update-the-login-credentials-username-and-password-for-the-api)
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
success
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/classic-vari-ostatus

# Get classicVARIO status parameter
```
GET /classicvario
```
GET
### Reading the Current Status from the classicVARIO+e[​](#reading-the-current-status-from-the-classicvarioe)
The following table explains the error codes and you can set the pump mode according to the values below:
| Pump modes |  | Error codes |
| --- | --- | --- |
| Value | Mode |  | Value | Mode |
| 4 | Bio Mode |  | 0 | ok, no error |
| 8 | Pulse Mode |  | 1 | rotor stuck |
| 16 | Manual Mode |  | 2 | air in the filter |
## Request[​](#request)
## Responses[​](#responses)
- 200

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/classic-vario-active

# Set classicVARIO+e on/off
```
POST /classicvario/active
```
POST
#### If you turn off the filter, it will stay off for a maximum of 10 minutes and then automatically turn on again.[​](#if-you-turn-off-the-filter-it-will-stay-off-for-a-maximum-of-10-minutes-and-then-automatically-turn-on-again)
This is used to turn it off when cleaning the equipment or when the feeder is in operation.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/classic-vario-bio

# Set Bio day/night mode
```
POST /classicvario/bio
```
POST
### Switch to Bio day/night mode[​](#switch-to-bio-daynight-mode)
You can set different speeds for the day and night phases.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/classic-vario-e

# classicVARIO+e
The EHEIM classicVARIO+e is an electronically controlled external filter with WiFi functionality that can be operated via smartphone, tablet, or PC/Mac. It combines the proven quality of classic filters with innovative wireless control and an exceptionally quiet BLDC pump. The pump performance can be continuously adjusted to meet the aquarium's needs. By connecting with other devices in the EHEIM Digital family, such as the autofeeder+ or LEDcontrol+e, the filter's function can be automatically coordinated, for example, by adjusting performance during feeding or to the day/night rhythm. Additional benefits of the classicVARIO+e include:
- Low power consumption (1.7-9.8 W) through power regulation
- Maintenance display and email reminders
- Permanently elastic silicone seal on the pump head
- Can be equipped with filter mats and/or loose filter media
- Includes installation accessories
- Suitable for fresh and salt water
The classicVARIO+e offers the highest quality, premium components, and carefully coordinated functions for optimal aquarium filtration.

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/classic-vario-manual

# Set Manual mode
```
POST /classicvario/manual
```
POST
### Switch to Manual mode[​](#switch-to-manual-mode)
You can set the speed as a percentage, from 0% to 100%. It will restore to the last known value if there is no rel_manual_motor_speed send.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/classic-vario-pulse

# Set Pulse mode
```
POST /classicvario/pulse
```
POST
### Switch to Pulse Mode[​](#switch-to-pulse-mode)
In this mode, the relative speed can be set for specific time intervals like in the UI.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/climacontrol

# climacontrol+
EHEIM climacontrol+ is an electronic temperature control device for aquariums, allowing users to cool down water on hot days or warm it up on cold days, as needed by the aquarium inhabitants. The device is controlled wirelessly via smartphone, tablet, or PC/MAC, and automatically cools or heats the water to maintain the set temperature. If the target temperature deviates by 2°C for more than 5 minutes, a warning email is sent. The device prevents overheating of aquarium water, which can be harmful to fish and other organisms. In marine aquariums, high temperatures can cause coral death, while in freshwater aquariums, it can lead to oxygen deficiency and algae growth. EHEIM climacontrol+ is energy-efficient and uses environmentally friendly refrigerant (R290). It comes in three sizes: S, M, and L, suitable for aquariums up to 500, 1000, and 2000 liters, respectively. The device should be operated with clean (filtered) water and placed with sufficient ventilation.

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/climacontrol-active

# Switching climacontrol+ on/off
```
POST /climacontrol/active
```
POST
### Switches the device on (1) or off(0)[​](#switches-the-device-on-1-or-off0)
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/climacontrol-bio

# Set Bio day/night mode
```
POST /climacontrol/bio
```
POST
### Switch to Bio day/night mode[​](#switch-to-bio-daynight-mode)
In Bio mode, you can set different temperature schedules for day and night. The nReduce value is relative to the target temperature (sollTemp) and uses a double value (e.g. 0.5).
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/climacontrol-config

# Set climacontrol+ configuration
```
POST /climacontrol/config
```
POST
### Configure the climacontrol Settings[​](#configure-the-climacontrol-settings)
You a able to change the Unit C° or F°, the temperature offset and the hysteresis for the temperatur regulation.
#### Be careful - If you switch the unit, you need to resend all configuration parameters with the recalculated values.[​](#be-careful---if-you-switch-the-unit-you-need-to-resend-all-configuration-parameters-with-the-recalculated-values)
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/climacontrol-manual

# Set Manual mode
```
POST /climacontrol/manual
```
POST
### Switch to Manual mode[​](#switch-to-manual-mode)
This API allows you to directly set the target temperature. If you call the endpoint without a temperature parameter, it will also switch to this mode.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/climacontrolstatus

# Get climacontrol status
```
GET /climacontrol
```
GET
### The response contains all device information in a single JSON array.[​](#the-response-contains-all-device-information-in-a-single-json-array)
The detailed informations of each parameter can be found in the schema description.
#### Be careful - If you switch the unit, you need to resend all configuration parameters with the recalculated values.[​](#be-careful---if-you-switch-the-unit-you-need-to-resend-all-configuration-parameters-with-the-recalculated-values)
## Request[​](#request)
## Responses[​](#responses)
- 200

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/doupdate

# Start software update
```
POST /doupdate
```
POST
### Perform a software update[​](#perform-a-software-update)
If a new version is available, the device will automatically perform the update by triggering the update by this API.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
When an update is available, the device will initiate the update process. This involves downloading and installing the latest firmware or software version to ensure optimal performance and access to new features.
The message "No new update found" indicates that the device is currently running the latest version of the firmware or software. There are no available updates at this time,
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/eheim-digital-api

# EHEIM Digital API
Welcome to the API documentation for EHEIM Digital products. This API provides comprehensive access to the full range of EHEIM Digital devices, enabling seamless integration and control. Whether you're building advanced aquarium management solutions or enhancing smart home capabilities, our API offers the flexibility and power you need.
The API supports all EHEIM Digital products running software version 2.0.1.x or later. With this documentation, you will find all the necessary resources, including detailed API calls, parameters, authentication methods, and usage examples to help you efficiently interact with your EHEIM devices.
Let’s dive in and explore how you can unlock the full potential of your EHEIM Digital products!
## Important Notes:[​](#important-notes)
Time Values: All time values are expressed in minutes from midnight. For example, if you want to turn a device on at 3 PM (15:00), you need to calculate: 15 hours * 60 minutes = 900 minutes.
Temperature Units: The temperature can be set in Celsius (°C) or Fahrenheit (°F), which you can choose on the Web UI. The selected unit will appear in the mUnit value:
- 0 = Celsius (e.g., 23.5°C is represented as 235 in the device settings)
- 1 = Fahrenheit (e.g., 72.5°F is represented as 725 in the device) Important: If you change the temperature unit, you'll need to resend all relevant parameters using the new unit.
nReduce Calculation: The value of nReduce is always based on the target temperature (sollTemp). For example, if your target temperature is 23°C and you want to lower it to 20.5°C at night, you calculate nReduce as: Target Temp - Desired Temp = nReduce ÷ 10 -> 230 (23°C) - 205 (20.5°C) = 25 (2.5°C)
Device Address (to value): Every request must include the MAC address of the target device in the "to" value field.
Boolean Values: When sending true/false values, use 1 for true and 0 for false.
## Authentication[​](#authentication)
- HTTP: Basic Auth
Example: username: api password: [default: admin]
| Security Scheme Type: | http |
| --- | --- |
| HTTP Authorization Scheme: | basic |
Contact
Eheim Support Service: [eheim.service@eheim.com](mailto:eheim.service@eheim.com)
URL: [https://eheim.com/de_DE/kundenservice/servicestellen/](https://eheim.com/de_DE/kundenservice/servicestellen/)
License

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/general

# general
All Eheim digital Devices support the same general endpoints from this chapter. You can read the general Device data or set for example the brightness of the LED.

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/get-le-dcontrol-acclimatisation

# Get acclimatization configuration
```
GET /light/daycycle/acclimatisation
```
GET
### Get acclimatization configuration[​](#get-acclimatization-configuration)
Retrieve the acclimatization configuration settings for the device. This feature ensures a gentle acclimatization phase, allowing your animals and plants to gradually adapt to the light and cycles.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/get-le-dcontrol-clouds

# Get cloud configuration
```
GET /light/daycycle/clouds
```
GET
### Get cloud configuration[​](#get-cloud-configuration)
Retrieve the current cloud configuration settings for the device.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/get-le-dcontrol-daycl

# Get Daycycle configuration
```
GET /light/daycycle/config
```
GET
### Get the Daycycle Configuration[​](#get-the-daycycle-configuration)
Retrieve the current Daycycle configuration settings for the device. This will provide information about the day and night cycles, including parameters such as light intensity, duration, and any specific time-based adjustments.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/get-le-dcontrol-moon

# Get Moon configuration
```
GET /light/daycycle/moon
```
GET
### Get Moon configuration[​](#get-moon-configuration)
Retrieve the current Moon configuration settings for the device. This will provide information about the moonlight simulation, including parameters such as minimal intensity, maximal intensity and natural moonlight cycle.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/get-le-dcontrol-multicollor

# Get Multicolor configuration
```
GET /light/daycycle/multicollor
```
GET
### Get the Multicolor configuration[​](#get-the-multicolor-configuration)
The Multicolor Configuration is part of the Daycycle Mode and allows you to read and set the Rainbow effect values.
### Important Notes:[​](#important-notes)
- To set color values, use HUE and saturation instead of RGB values.
- The HUE value controls the color tone, and saturation defines the intensity of the color. This setup enables dynamic color transitions and effects based on the Daycycle, including a rainbow effect across the specified time periods.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/le-dcontrol-accl

# Set acclimatization configuration
```
POST /light/daycycle/acclimatisation
```
POST
### To Enable Acclimatization mode[​](#to-enable-acclimatization-mode)
Follow these API to activate Acclimatization mode.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/le-dcontrol-clouds

# Set cloud configuration
```
POST /light/daycycle/clouds
```
POST
### Set the cloud configuration[​](#set-the-cloud-configuration)
To set the cloud configuration, specify the following parameters:
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/le-dcontrol-config

# Set Daycycle configuration
```
POST /light/daycycle/config
```
POST
### Set the Daycycle configuration[​](#set-the-daycycle-configuration)
To set the Daycycle configuration, provide an array with up to 30 value points for a day. Each point should include the following parameters:
- Time: The specific time of day (in the appropriate format).
- Channel1, Channel2, Channel3: The values for each channel at that time. Each value point array should be structured as: [Time, channel1, channel2, channel3]. For example: [[0, 50, 60, 70], [600, 60, 70, 80], [1200, 70, 80, 90], ...] Send this array to configure the Daycycle for the device.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/le-dcontrol-daycycle

# Set Daycycle mode
```
POST /light/daycycle
```
POST
### Switching to Daycycle mode[​](#switching-to-daycycle-mode)
To switch to Daycycle mode, send a request to the device to activate this mode.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/le-dcontrol-manual

# Set Manual mode
```
POST /light/manual
```
POST
### Set the Channel Values manually[​](#set-the-channel-values-manually)
To set the channel values manually, you need to provide a request that specifies the desired values for each channel. You can adjust the values for each channel independently, with each value ranging from 0% to 100%.
If no parameters other than "to" is sent, the device will automatically use the last known values.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/le-dcontrol-moon

# Set Moon parameters
```
POST /light/daycycle/moon
```
POST
### Set the Moon parameters[​](#set-the-moon-parameters)
To set the moon parameters, you need to configure the following settings:
- Moonlight Intensity: Set the maximum intensity (0 to 100) to define the brightest level of moonlight. Set the minimum intensity (0 to 100) to define the dimmest level of moonlight.
- Moonlight on/off: Turn moonlight on or off to enable or disable the moonlight simulation.
- Moon Cycle on/off: Enable or disable the moon cycle simulation (on/off). When enabled, the moonlight will follow the natural lunar phases.
This will apply the specified moonlight and moon cycle configurations. For example:
```
  {      "moonlight_intensity":         { "max": 80, "min": 20 },      "moonlight_on": 1,      "moon_cycle_on": 1    }
```
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/le-dcontrol-series

# LEDcontrol series
### LEDcontrol+, LEDcontrol+e, RGBcontrol+e, classicLEDcontrol+e[​](#ledcontrol-ledcontrole-rgbcontrole-classicledcontrole)
The classicLEDcontrol has 2 channels, the aquaFamily has 4 channels and all other Devices have 3 channels.
| RGBcontrol+e | classicLEDcontrol+e | LEDcontrol+e | LEDcontrol+ |
| --- | --- | --- | --- |

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/light-current-values

# Get Current channel values
```
GET /light
```
GET
## Get the Current Device Settings and Channel Values[​](#get-the-current-device-settings-and-channel-values)
This request gives you on JSON Object:
- CCV: Contains the current channel values.
```
# Example:  {    "title": "CCV",    "from": "24:4C:AB:02:4E:34",    "currentValues": [      81,      47,      53]
```
Each value corresponds to a specific channel and ranges from 0% to 100%.
#### Channel Configuration[​](#channel-configuration)
Depending on the LED light configuration, as specified in the first entry of the JSON USRDTA parameter tankconfig, the channels are mapped to the light colors as follows:
| Configuration | Channel 1 | Channel 2 | Channel 3 |
| --- | --- | --- | --- |
| FRESH_DAYLIGHT | White | not used | not used |
| FRESH_PLANTS | White | Plants gold | Royal Blue |
| MARINE_ACTINIC | not used | not used | Royal Blue |
| MARINE_HYBRID | White | not used | Royal Blue |
| RGB_AMBIENT | Red | Green | Royal Blue |
| RGB_LIGHT | Red | Green | Royal Blue |
| All classicLED lights | only one channel per light | only one channel per light |  |
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/mesh-liste

# Get Mesh list
```
GET /devicelist
```
GET
## Get Mesh list with device MAC and IP addresses[​](#get-mesh-list-with-device-mac-and-ip-addresses)
This provides a list of all device MAC and IP addresses that are connected to the master system. Each entry corresponds to a unique device, identified by its MAC and IP address, allowing you to see all devices currently linked to the master for easy identification and management.
## Responses[​](#responses)
- 200
List of all devices

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/p-hcontrol-e

# pHcontrol+e
EHEIM pHcontrol+e is a smart controller that monitors and adjusts the pH level in aquariums via smartphone, tablet, or PC/MAC. A pH sensor measures the current water pH, and the pHcontrol+e automatically provides the necessary CO2 supply by controlling a solenoid valve connected to a CO2 system. To operate, you need to connect a CO2 system (CO2 bottle with pressure reducer, solenoid valve, and CO2 diffuser). The pHcontrol+e features day/night control and can be linked to the EHEIM LEDcontrol+e lighting control (see EHEIM DIGITAL Family). Plants in your aquarium need CO2 as an important nutrient, along with light, nitrogen, phosphate, trace elements, etc. The better they thrive, the more oxygen they release, which fish need to breathe. Thus, by adding CO2, the pHcontrol+e indirectly provides oxygen and the optimal pH value for your fish, typically between pH 6 and pH 8 (neutral guideline: pH 7). The device offers a measuring range of pH 0 to pH 14, a control range of pH 6 to pH 9, and features guided calibration of the pH sensor. It provides reminders for water tests and calibration, warnings for pH deviations, and an indication when the EHEIM pHsensor needs replacement. The new improved chip generation ensures the best performance, high efficiency, stable connection, and large storage capacity.

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/p-hcontrol-status

# pHcontrol status parameter
```
GET /phcontrol
```
GET
### This retrieves the current status from the pHcontrol+e device.[​](#this-retrieves-the-current-status-from-the-phcontrole-device)
## Request[​](#request)
## Responses[​](#responses)
- 200

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/phcontrol-active

# Switching pHcontrol on/off
```
POST /phcontrol/active
```
POST
### Switching pHcontrol on/off[​](#switching-phcontrol-onoff)
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/phcontrol-bio

# Bio day/night mode
```
POST /phcontrol/bio
```
POST
### Switch to Bio Mode[​](#switch-to-bio-mode)
The Bio Mode is designed to optimize the pH control system for biological processes, where maintaining a stable pH for day and night is crucial for the health of aquatic life. The expert mode gets switched automatically if you send a schedule, it switches to expert mode but if the scedule property is missing, it switches back to simple mode.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/phcontrol-manual

# Manual pH mode
```
POST /phcontrol/manual
```
POST
### Manual Mode[​](#manual-mode)
This mode allows you to set a fixed pH value that the system will maintain continuously.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/professionel-5-bio-mode

# Set Bio Mode
```
POST /professionel5e/bio
```
### Value and Version Table[​](#value-and-version-table)
#### Liter’s Value Table[​](#liters-value-table)
The Flow Rate value ranges from 0 to 14, and this range corresponds to a specific number of liters, depending on the filter model. The table below illustrates how the flow rate values map to liters based on the filter model.
| flowRate | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Filter 350 | 400 | 440 | 480 | 515 | 550 | 585 | 620 | 650 | 680 | 710 | 740 | 770 | 800 | 830 | 860 |
| Filter 450 | 400 | 460 | 515 | 565 | 610 | 650 | 690 | 730 | 770 | 805 | 840 | 875 | 910 | 945 | 980 |
| Filter 600T & 700 | 400 | 470 | 540 | 600 | 650 | 700 | 745 | 785 | 825 | 865 | 905 | 945 | 985 | 1025 | 1065 |
#### Gallon's value Table for US Market[​](#gallons-value-table-for-us-market)
The Flow Rate value can range from 0 to 14 and corresponds to a specific number of gallons, depending on the filter model, as shown in the table below:
| flowRate | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Filter 350 | 110 | 120 | 130 | 140 | 145 | 155 | 165 | 175 | 180 | 190 | 195 | 205 | 215 | 220 | 230 |
| Filter 450 | 110 | 125 | 140 | 150 | 165 | 175 | 185 | 195 | 205 | 215 | 225 | 235 | 240 | 250 | 260 |
| Filter 600T & 700 | 110 | 125 | 145 | 165 | 175 | 185 | 200 | 210 | 220 | 230 | 240 | 250 | 260 | 275 | 285 |
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/professionel-5-e

# professionel5e
The EHEIM professional 5e is a state-of-the-art electronic external filter with integrated WiFi functionality. It offers aquarists maximum convenience, quality, and performance. Through wireless control via smartphone, tablet, or PC/MAC, it can be individually programmed and monitored. The freely configurable modes include constant flow, bio mode, pulse mode, and manual mode. The electronic flow regulation significantly extends the cleaning intervals for the biological filter material. The filter can also be linked with other devices, such as the LEDcontrol+ lighting control. Additional advantages include the large, directly accessible pre-filter for quick removal of mechanical dirt, the large container and filter volume, and the high-quality, wear-free ceramic shaft with ceramic bearings for extremely quiet operation. The electronics continuously monitor the system, automatically remove air, and attempt to resolve error causes independently. The professional 5e is available in four models for aquariums from 180 to 700 liters, including a thermal filter with integrated heater. The Model 350 comes complete with filter media and offers filter function extension via a rotary knob (Xtender). The filter is suitable for fresh and salt water (except thermal filter), comes with installation accessories, and includes a 3-year warranty. The WiFi function can be deactivated after configuration without affecting the filter function.

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/professionel-5-e-status

# Get professionel5e status
```
GET /professionel5e
```
### Value and Version Table[​](#value-and-version-table)
#### Liter’s Value Table[​](#liters-value-table)
The Flow Rate value ranges from 0 to 14, and this range corresponds to a specific number of liters, depending on the filter model. The table below illustrates how the flow rate values map to liters based on the filter model.
| flowRate | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Filter 350 | 400 | 440 | 480 | 515 | 550 | 585 | 620 | 650 | 680 | 710 | 740 | 770 | 800 | 830 | 860 |
| Filter 450 | 400 | 460 | 515 | 565 | 610 | 650 | 690 | 730 | 770 | 805 | 840 | 875 | 910 | 945 | 980 |
| Filter 600T & 700 | 400 | 470 | 540 | 600 | 650 | 700 | 745 | 785 | 825 | 865 | 905 | 945 | 985 | 1025 | 1065 |
#### Gallon's value Table for US Market[​](#gallons-value-table-for-us-market)
The Flow Rate value can range from 0 to 14 and corresponds to a specific number of gallons, depending on the filter model, as shown in the table below:
| flowRate | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Filter 350 | 110 | 120 | 130 | 140 | 145 | 155 | 165 | 175 | 180 | 190 | 195 | 205 | 215 | 220 | 230 |
| Filter 450 | 110 | 125 | 140 | 150 | 165 | 175 | 185 | 195 | 205 | 215 | 225 | 235 | 240 | 250 | 260 |
| Filter 600T & 700 | 110 | 125 | 145 | 165 | 175 | 185 | 200 | 210 | 220 | 230 | 240 | 250 | 260 | 275 | 285 |
## Request[​](#request)
## Responses[​](#responses)
- 200

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/professionel-5-econstant-mode

# Set Constant Flow mode
```
POST /professionel5e/constant
```
### Value and Version Table[​](#value-and-version-table)
#### Liter’s Value Table[​](#liters-value-table)
The Flow Rate value ranges from 0 to 14, and this range corresponds to a specific number of liters, depending on the filter model. The table below illustrates how the flow rate values map to liters based on the filter model.
| flowRate | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Filter 350 | 400 | 440 | 480 | 515 | 550 | 585 | 620 | 650 | 680 | 710 | 740 | 770 | 800 | 830 | 860 |
| Filter 450 | 400 | 460 | 515 | 565 | 610 | 650 | 690 | 730 | 770 | 805 | 840 | 875 | 910 | 945 | 980 |
| Filter 600T & 700 | 400 | 470 | 540 | 600 | 650 | 700 | 745 | 785 | 825 | 865 | 905 | 945 | 985 | 1025 | 1065 |
#### Gallon's value Table for US Market[​](#gallons-value-table-for-us-market)
The Flow Rate value can range from 0 to 14 and corresponds to a specific number of gallons, depending on the filter model, as shown in the table below:
| flowRate | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Filter 350 | 110 | 120 | 130 | 140 | 145 | 155 | 165 | 175 | 180 | 190 | 195 | 205 | 215 | 220 | 230 |
| Filter 450 | 110 | 125 | 140 | 150 | 165 | 175 | 185 | 195 | 205 | 215 | 225 | 235 | 240 | 250 | 260 |
| Filter 600T & 700 | 110 | 125 | 145 | 165 | 175 | 185 | 200 | 210 | 220 | 230 | 240 | 250 | 260 | 275 | 285 |
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/professionel-5-emanual-mode

# Set Manual mode
```
POST /professionel5e/manual
```
#### Frequency Table[​](#frequency-table)
All values are given in Hz and must be multiplied by 100 to obtain the correct frequency value. For example, a frequency of 35 Hz would be multiplied as follows: 5 Hz × 100 = 3500 frequency value.
| steps | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Filter 350 | 35 | 37.5 | 40.5 | 43 | 45.5 | 48 | 51 | 53.5 | 56 | 59 | 61.5 | 64 | 66.5 | 69.5 | 72 |
| Filter 450 | 35 | 38 | 41 | 44 | 46.5 | 49.5 | 52.5 | 55.5 | 58.5 | 61.5 | 64.5 | 67 | 70 | 73 | 76 |
| Filter 600T & 700 | 35 | 38 | 41.5 | 44.5 | 48 | 51 | 54 | 57.5 | 60.5 | 64 | 67 | 70 | 73.5 | 76.5 | 80 |
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/professionel-5-pump

# Set professionel5e on/off
```
POST /professionel5e/active
```
POST
### Switches the Filter on/off[​](#switches-the-filter-onoff)
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/professionel-5-pump-mode

# Set Pulse mode
```
POST /professionel5e/pulse
```
### Value and Version Table[​](#value-and-version-table)
#### Liter’s Value Table[​](#liters-value-table)
The Flow Rate value ranges from 0 to 14, and this range corresponds to a specific number of liters, depending on the filter model. The table below illustrates how the flow rate values map to liters based on the filter model.
| flowRate | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Filter 350 | 400 | 440 | 480 | 515 | 550 | 585 | 620 | 650 | 680 | 710 | 740 | 770 | 800 | 830 | 860 |
| Filter 450 | 400 | 460 | 515 | 565 | 610 | 650 | 690 | 730 | 770 | 805 | 840 | 875 | 910 | 945 | 980 |
| Filter 600T & 700 | 400 | 470 | 540 | 600 | 650 | 700 | 745 | 785 | 825 | 865 | 905 | 945 | 985 | 1025 | 1065 |
#### Gallon's value Table for US Market[​](#gallons-value-table-for-us-market)
The Flow Rate value can range from 0 to 14 and corresponds to a specific number of gallons, depending on the filter model, as shown in the table below:
| flowRate | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Filter 350 | 110 | 120 | 130 | 140 | 145 | 155 | 165 | 175 | 180 | 190 | 195 | 205 | 215 | 220 | 230 |
| Filter 450 | 110 | 125 | 140 | 150 | 165 | 175 | 185 | 195 | 205 | 215 | 225 | 235 | 240 | 250 | 260 |
| Filter 600T & 700 | 110 | 125 | 145 | 165 | 175 | 185 | 200 | 210 | 220 | 230 | 240 | 250 | 260 | 275 | 285 |
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/reeflex-u-vstatus

# reeflexUV Status Parameter
```
GET /reeflexuv
```
GET
### The response contains all the device information in a single JSON array.[​](#the-response-contains-all-the-device-information-in-a-single-json-array)
The detailed information for each parameter can be found in the schema description.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/reeflex-uv-active

# Switching reeflexUV on/off
```
POST /reeflexuv/active
```
POST
### This endpoint can activate or deacitvate the device.[ ​](#this-endpoint-can-activate-or-deacitvate-the-device)
This will keep the last selected mode
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/reeflex-uv-boost

# Boost for reeflexUV
```
POST /reeflexuv/boost
```
POST
### The Boost Mode is designed to keep the reeflexUV system active for a specific duration.[​](#the-boost-mode-is-designed-to-keep-the-reeflexuv-system-active-for-a-specific-duration)
Ensuring that the UVC lamp remains on without being turned off. This mode can be used to provide extended operation, typically for additional treatment or performance, without interruptions. Can be turned on for max. 2 weeks => 20160 minutes
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/reeflex-uv-daycycle

# Set daycycle mode for reeflexUV
```
POST /reeflexuv/daycycle
```
POST
### Configure the ReeflexUV device in daycycle mode[​](#configure-the-reeflexuv-device-in-daycycle-mode)
The only required fields are the to parameter (specifying the target device) and the start time, which is the time in minutes from midnight. The daily burn time is optional and, if not provided, will automatically be set to 720 minutes (12 hours) by default.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/reeflex-uv-e

# reeflexUV+e
EHEIM reeflexUV+e is a WiFi-controlled UV clarifier that reduces or eliminates harmful microorganisms and removes water turbidity. The device uses a patented reflector technology that significantly enhances the germicidal UV-C radiation, making it twice as effective as conventional UV clarifiers while saving energy. The water flows directly past the UV-C lamp without detours, minimizing power loss. The reeflexUV+e can be coupled with EHEIM Digital Family products and controlled via WiFi-enabled devices (smartphone, tablet, notebook, etc.). Users can choose various modes, set times and breaks, and switch to a booster mode for severe parasite infestations. The device should be used in addition to a filter to reduce microorganisms (germs, algae spores, etc.) in the aquarium. Four models are available for aquariums ranging from 300 to 2000 liters. The device features an AUTO-OFF safety switch-off during lamp replacement and is suitable for both freshwater and saltwater aquariums.

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/reeflex-uv-pause

# Pause for reeflexUV
```
POST /reeflexuv/pause
```
POST
### The pause time can be activated to temporarily stop the UVC function for a specific period.[​](#the-pause-time-can-be-activated-to-temporarily-stop-the-uvc-function-for-a-specific-period)
This allows the system to pause its operation without turning off completely, resuming after the defined duration. The time is caluclated in minutes.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/set-le-dcontrol-multicollor

# Set Multicolor configuration
```
POST /light/daycycle/multicollor
```
POST
### Set the Multicolor configuration[​](#set-the-multicolor-configuration)
To set the multicolor configuration, you need to define a nested array that includes the color values and additional parameters:
- [R, G, B, HSV, Saturation]: R, G, B: The RGB values (for reference purposes). HSV: The Hue, Saturation, and Value (HSV) color model. This should be used to change the color effect instead of the RGB values. Saturation: Defines the intensity of the color.
- Duration: The duration of the effect in minutes (optional).
- Rainbow Effect (On/Off): 1 to turn the rainbow effect on. 0 to turn the rainbow effect off.
- Scene Number: Set the scene number to 2 to enable multicolor.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/thermocontrol-active

# Switching thermocontrol+e on/off
```
POST /thermocontrol/active
```
POST
### Switches the device on (1) or off(0)[​](#switches-the-device-on-1-or-off0)
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/thermocontrol-bio

# Set Bio day/night mode
```
POST /thermocontrol/bio
```
POST
### Switch to Bio day/night mode[​](#switch-to-bio-daynight-mode)
In Bio mode, you can set different temperature schedules for day and night. The nReduce value is relative to the target temperature (sollTemp) and uses a double value (e.g. 0.5).
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/thermocontrol-config

# Set thermocontrol+e configuration
```
POST /thermocontrol/config
```
POST
### Configuration Parameters[​](#configuration-parameters)
You can set whether the device uses °F or °C. If you switch the unit, you must resend all values in the correctly calculated format to ensure the device uses the correct ones.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/thermocontrol-e

# thermocontrol+e
The EHEIM thermocontrol+ e is an innovative, intelligently designed aquarium heater with digital control via WiFi. Users can precisely set the temperature from 18 to 32°C using a smartphone, tablet, or PC/MAC. The electronics accurately measure and maintain the target temperature, and if it deviates by ±2°C, an email notification is immediately sent. The thermocontrol+ e can be synchronized with filter activity or lighting, allowing wireless connection to the EHEIM professionel 5e filter or LEDcontrol+. The heater's construction features a special laboratory glass sheath, flawless workmanship, high-quality materials, and absolute reliability. It comes with a 3-year warranty and is available in 4 sizes for aquariums from 200 to 1000 liters. Key features include:
- Temperature control accuracy of ±0.5°C
- Indicator lights for heating function and operating status
- Smart linking with other EHEIM.digital devices for temperature adjustment based on water flow or day/night cycles
- Waterproof (IPX8) design - immerse up to the marking for optimal WiFi reception
- Dry-run protection (Thermo Safety Control)
- Comfort cable length of approx. 170 cm
- Includes double suction holder
- Suitable for fresh and saltwater

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/thermocontrol-manual

# Set Manual mode
```
POST /thermocontrol/manual
```
POST
### Switch to Manual temperature mode[​](#switch-to-manual-temperature-mode)
This API allows you to directly set the target temperature. If you call the endpoint without a temperature parameter, it will switch to this mode anyways.
## Request[​](#request)
## Responses[​](#responses)
- 200
- 400
- 401
Request was successfull
Bad Request
Unauthorized

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/thermocontrol-status

# Get status parameters
```
GET /thermocontrol
```
GET
### Get status parameters of the thermoctontrol+e[​](#get-status-parameters-of-the-thermoctontrole)
This endpoint reads the current status from the thermocontrol+e device. It retrieves real-time information, such as temperature settings, operational modes, and other important parameters, allowing users to monitor and manage the device effectively.
Depending on the unit you have chosen, you will need to calculate the temperatures accordingly:
- If you selected Celsius (°C), temperatures should be calculated and represented in degrees Celsius.
- If you selected Fahrenheit (°F), temperatures should be calculated and represented in degrees Fahrenheit. Ensure to convert the values correctly based on the chosen unit to maintain accurate readings.
## Request[​](#request)
## Responses[​](#responses)
- 200

---

## Quelle: https://api.eheimdigital.com/docs/eheim_digital_api/userdata

# Get Device configuration
```
GET /userdata
```
GET
### This endpoint provides detailed information about the device, including:[​](#this-endpoint-provides-detailed-information-about-the-device-including)
- Device Name
- Software version
- Whether an update is available
- Timezone
and other important details...
## Request[​](#request)
## Responses[​](#responses)
- 200

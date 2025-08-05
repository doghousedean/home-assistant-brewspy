# BrewSpy Home Assistant Integration

Monitors fermentation data from BrewSpy in Home Assistant.  
Displays gravity, temperature, battery status and more.

Visit https://brewspy.app to get your device token.

## Features

- Displays temperature, gravity, battery level, and other readings from BrewSpy
- Easy setup with just your device token
- Optional device name customization

## Setup Instructions

1. Get your BrewSpy API token:  
   Log into [https://brewspy.app/app](https://brewspy.app/app) and copy the token from your device's Export URL.

2. In Home Assistant:
   - Go to **Settings > Devices & Services > Add Integration**
   - Search for **BrewSpy**
   - Paste your token in the "Device ID" field

3. Done! Your device sensors will now appear in Home Assistant.

## Notes

- Only the most recent reading is retrieved at this time.
- Data updates periodically when HA refreshes sensors.

This integration is not affiliated with BrewSpy.

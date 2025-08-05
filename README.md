# BrewSpy Home Assistant Integration

Easily connect your BrewSpy fermentation monitor to Home Assistant and keep an eye on gravity, temperature, battery levels, and more—right from your dashboard.

> ⚠️ This integration is community-developed and not officially affiliated with BrewSpy.

---
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=flat-square)](https://hacs.xyz/)

Connect your Home Assistant to BrewSpy to monitor gravity, temperature, battery and more from your fermentation devices.

## Installation (via HACS)
1. Add this repo as a [custom repository](https://hacs.xyz/docs/faq/custom_repositories) in HACS.
2. Search for "BrewSpy" in HACS integrations and install.
3. Restart Home Assistant.
4. Go to *Settings > Devices & Services > Add Integration* and search for **BrewSpy**.
5. Enter your device token from [brewspy.app](https://brewspy.app/app).


### Option 2: Manual

1. Download or clone this repository.
2. Copy the `brewspy` folder into your Home Assistant `custom_components` directory.
3. Restart Home Assistant and add the integration as above.

---

## 🔧 Configuration

Get your **Device ID Token** from the BrewSpy website and paste it when adding the integration.

After installation:

1. Log into [brewspy.app](https://brewspy.app/app)
2. Copy the API token for your device.
3. When adding the integration, paste this token as the “Device ID”.

You can also edit the token later via the integration’s options.

---

## 📊 Sensors Provided

- Gravity
- Temperature (°C)
- Tilt angle
- Battery voltage
- Battery percentage (based on voltage curve)
- Wi-Fi RSSI
- Timestamp of last update

---

## 🧪 Known Issues

- Only the most recent reading is retrieved
- Multi-device support is not yet implemented

---

## 🤝 Contributing

PRs are welcome! This is a very early version and any improvements, feature requests, or fixes are appreciated.

---

## 📜 License

MIT

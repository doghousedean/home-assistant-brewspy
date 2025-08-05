# BrewSpy Home Assistant Integration

Easily connect your BrewSpy fermentation monitor to Home Assistant and keep an eye on gravity, temperature, battery levels, and more—right from your dashboard.

> ⚠️ This integration is community-developed and not officially affiliated with BrewSpy.

---

## 📦 Installation

### Option 1: HACS (Recommended)

1. Add this repository to HACS:
   - Go to **HACS > Integrations > ⋮ (top right) > Custom repositories**
   - Add the GitHub repo URL (e.g. `https://github.com/doghousedean/home-assistant-brewspy`) as type **Integration**
2. Search for **BrewSpy** in HACS and install it.
3. Restart Home Assistant.
4. Add the integration via **Settings > Devices & Services > + Add Integration** and search for “BrewSpy”.

### Option 2: Manual

1. Download or clone this repository.
2. Copy the `brewspy` folder into your Home Assistant `custom_components` directory.
3. Restart Home Assistant and add the integration as above.

---

## 🔧 Configuration

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

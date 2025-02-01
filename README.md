# Network Device Scanner 🔧

A Python script that scans your local network, retrieves active devices from the ARP table, and maps MAC address prefixes to known device names using an RTF file.

## 🚀 Features
- Lists all devices connected to the network.
- Extracts MAC addresses and their corresponding manufacturers.
- Supports **Windows, Linux, and macOS**.
- Parses device names from an **RTF file**.
- Uses Python and the `subprocess` module to execute network scanning commands.

---

## 🛠 Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Real-J/network-device-scanner.git
cd network-device-scanner
```

### **2️⃣ Install Dependencies**
Ensure you have Python **3.7+** installed. Then, install the required packages:
```sh
pip install pandas striprtf
```

---

## 📌 Usage
1. **Prepare the RTF file**:
   - The RTF file should contain entries in the format:
     ```
     DeviceName, MAC_Prefix
     Printer, 00:1A:2B
     SmartTV, 78:4F:43
     ```

2. **Run the script**:
   ```sh
   python scanner.py
   ```
   - The script will read the ARP table, extract connected devices, and map them using the RTF file.

---

## 👌 Example Output
```
Raw ARP output:
? (192.168.1.10) at 00:1A:2B:3C:4D:5E on en0
? (192.168.1.20) at 78:4F:43:12:34:56 on en0

Devices connected to your network:
-----------------------------------
      Name       | Hostname/IP Address   | MAC Address
------------------------------------------------------
 Printer        | Unknown (192.168.1.10) | 00:1A:2B:3C:4D:5E
 SmartTV        | Unknown (192.168.1.20) | 78:4F:43:12:34:56
```

---

## ⚙ Supported Platforms
| OS      | Status |
|---------|--------|
| Windows | ✅ Supported (`arp -a`) |
| Linux   | ✅ Supported (`ip -4 neigh`) |
| macOS   | ✅ Supported (`arp -a`) |

---

## 💜 License
This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it.

---

## 🤝 Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit: `git commit -m "Description of changes"`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request. 🚀

---

## 📧 Contact
For questions or suggestions, reach out via:
- **Email**: your.email@example.com
- **GitHub Issues**: [Open an issue](https://github.com/yourusername/network-device-scanner/issues)


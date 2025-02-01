import subprocess
import re
import pandas as pd
from striprtf.striprtf import rtf_to_text
import platform

def load_names_from_file(filename):
    """Load names and MAC address prefixes from an RTF file."""
    try:
        with open(filename, 'rb') as file:  # Open in binary mode
            rtf_content = file.read().decode('utf-8', errors='ignore')  # Decode with error handling

        plain_text = rtf_to_text(rtf_content)
        
        name_map = {}
        for line in plain_text.splitlines():
            if ',' in line:  # Assumes 'Name,MAC_Prefix' format
                name, mac_prefix = line.split(',')
                name_map[mac_prefix.strip().lower()] = name.strip()
        return name_map

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return {}

def get_arp_command():
    """Returns the correct ARP command based on OS."""
    os_type = platform.system().lower()
    if os_type == "windows":
        return ["arp", "-a"]
    elif os_type == "linux":
        return ["ip", "-4", "neigh"]
    elif os_type == "darwin":  # macOS
        return ["arp", "-a"]
    else:
        raise RuntimeError(f"Unsupported OS: {os_type}")

def list_network_devices(name_map_file="/Users/mathew/Desktop/Unt.rtf"):
    try:
        # Load the name map from the provided file
        name_map = load_names_from_file(name_map_file)

        # Determine the correct command
        command = get_arp_command()

        # Run the command and capture output
        output = subprocess.check_output(command, stderr=subprocess.DEVNULL).decode('utf-8')

        print("Raw ARP output:\n", output)

        devices = []
        for line in output.splitlines():
            # Regex to capture hostname, IP, and MAC address
            match = re.search(r'(\S+)?\s+\((\d+\.\d+\.\d+\.\d+)\)\s+at\s+((?:[0-9a-fA-F]{1,2}[:-]){5}[0-9a-fA-F]{1,2})', line)
            if match:
                hostname = match.group(1) or "Unknown"
                ip = match.group(2)
                mac = match.group(3)

                # Skip broadcast addresses
                if mac.lower() != "ff:ff:ff:ff:ff:ff":
                    mac_prefix = mac[:7].lower().replace("-", ":")  # OUI = first 6 chars
                    name = name_map.get(mac_prefix, "Unknown Device")
                    
                    devices.append({
                        "Name": name,
                        "Hostname/IP Address": f"{hostname} ({ip})",
                        "MAC Address": mac
                    })

        if devices:
            df = pd.DataFrame(devices)
            print("\nDevices connected to your network:")
            print("-----------------------------------")
            print(df.to_string(index=False))
        else:
            print("No devices found.")

    except FileNotFoundError:
        print("Error: 'arp' command not found. Ensure it is installed and accessible.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing arp command: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

list_network_devices()

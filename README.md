# Packet Sniffer Tool

## Overview

This project is a simple educational packet sniffer built using Python and Scapy.
It captures live network packets and displays useful information such as:

* Source IP Address
* Destination IP Address
* Protocol Type
* Port Numbers
* Payload Preview

This project is intended only for educational and authorized testing purposes.

---

## Features

* Real-time packet capture
* IPv4 packet analysis
* TCP and UDP protocol detection
* Source and destination port extraction
* Payload preview display
* Exception handling
* Lightweight console-based interface

---

## Technologies Used

* Python
* Scapy
* Npcap (Windows)

---

## Installation

### 1. Clone the Repository

```bash
https://github.com/SoumiBandyopadhyay/PRODIGY_CS_05
cd packet-sniffer
```

---

### 2. Install Required Package

```bash
pip install scapy
```

---

### 3. Install Npcap (Windows Only)

Download and install:

[https://npcap.com/](https://npcap.com/)

During installation, enable:

* Install Npcap in WinPcap API-compatible Mode

---

## Project Structure

```text
packet-sniffer/
│
├── packet_sniffer.py
├── README.md
└── requirements.txt
```

---

## Running the Program

### Windows

```bash
py packet_sniffer.py
```

### Linux/macOS

```bash
sudo python3 packet_sniffer.py
```

---

## Example Output

```text
============================================================
Source IP       : 192.168.1.5
Destination IP  : 142.250.183.78
Protocol Number : 6
Protocol        : TCP
Source Port     : 52341
Destination Port: 443

Payload Preview:
GET / HTTP/1.1
============================================================
```

---

## Requirements

Create a `requirements.txt` file:

```text
scapy
```

---

## Disclaimer

This tool is developed strictly for:

* Educational purposes
* Learning network analysis
* Authorized security testing

Do not use this tool on networks or systems without permission.
Unauthorized packet sniffing may violate privacy laws and cybersecurity regulations.

---

## Future Improvements

* Packet filtering
* GUI interface
* Save packets to log files
* DNS analysis
* HTTP request detection
* Live traffic statistics
* Colorized console output

---

## Author

Soumi Bandyopadhyay

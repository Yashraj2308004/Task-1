# 🔍 Local Network Scanning Task (Internship)

This folder contains screenshots of local network scanning and enumeration task performed by me as part of my cybersecurity internship.

## 🛠️ Tools Used

- `ifconfig` – From this I got my local ip and subnet also for further scanning.
- `nmap` – Using this I performed basic scanning of whole subnet and tried running some scripts also on the open ports which I found.
- `zenmap` – Scanned network in my windows machine with GUI.
- `bettercap` – performed network scanning and host discovery and also tried arp spoofing which I found while I was searching for more tools for network scanning.
- `ettercap` – With this also I performed network scanning and tried sniffing passwords and usernam on http website but didn't worked on https websites.
- `enum4linux` – Somewhere in one article I got to know aboout this so I performed smb enumaration with this on of my device where I found smb port open.

## 🤖 Automated Host Discovery (Python Script)

- I also tried to make automatic host discovery by scanning my whole subnet using python.
- I took help from google, AI and some you tube videos to create it.
- This script performs a basic ping sweep to discover live hosts on the local subnet automatically.

### Features:
- It will Auto-detect your subnet based on your local IP.
- And will pings all addresses from `.1` to `.254`
- Displays only live (reachable) hosts.

- I tried to add port scanning for live hosts but some concepts I didn't understood for now so I will try to first understand it and then will try to add that too in    this script.

## ✅ Conclusion

- This task helped me explore both manual and automated approaches to local network scanning.
- I also learned about tools like nmap , bettercap , ettercap.

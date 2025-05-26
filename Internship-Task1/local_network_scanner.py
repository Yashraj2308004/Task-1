import subprocess
import socket

def get_subnet():
    #This function returns the subnet from your ip like "192.168.1" or "192.168.0"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    print(f"Your subnet is : {".".join(ip.split('.')[:3])}")
    return ".".join(ip.split('.')[:3])

def ping_host(ip):
    try:
        output = subprocess.run(
            ["ping", "-n", "1", "-w", "1000", ip], 
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return output.returncode == 0
    except Exception as e:
        return False

def ping_sweep(subnet):
    print(f"[*] Scanning subnet {subnet}.1-254 for live hosts...\n")
    for i in range(1, 255):
        ip = f"{subnet}.{i}"
        if ping_host(ip):
            print(f"[+] Host up: {ip}")

ping_sweep(get_subnet()) # here from the function we will get subnet which will be passed in ping_sweep function 

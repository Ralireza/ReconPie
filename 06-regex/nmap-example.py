import nmap

ip = "185.188.104.10"  # Replace with the IP address you want to scan

nm = nmap.PortScanner()
nm.scan(ip, arguments="-p 1-65535 -T4")  # Scan all ports (1-65535) with aggressive timing (-T4)

for host in nm.all_hosts():
    print("Open ports for {}:".format(host))
    for port in nm[host]["tcp"].keys():
        if nm[host]["tcp"][port]["state"] == "open":
            print("Port {} is open".format(port))

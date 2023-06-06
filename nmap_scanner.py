import nmap

class NmapPortScanner:
    def scan_port(ip):
        nm = nmap.PortScanner()
        nm.scan(ip, arguments="-p 1-65535 -T4")  # Scan all ports (1-65535) with aggressive timing (-T4)
        results = []
        for host in nm.all_hosts():
            print("Open ports for {}:".format(host))
            for port in nm[host]["tcp"].keys():
                if nm[host]["tcp"][port]["state"] == "open":
                    print("Port {} is open".format(port))
                    results.append(port)
                    
        return results

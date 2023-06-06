import socket

class SocketIp:
    def GetIpFromDomain(domain):
        # Use the gethostbyname() function from the socket library to get the IP address for the specified domain
        ip_address = socket.gethostbyname(domain)
        return f"The IP address of {domain} is {ip_address}"

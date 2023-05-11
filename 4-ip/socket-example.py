import socket

# Replace "example.com" with the domain name you want to map to an IP address
domain = "hackerone.com"

# Use the gethostbyname() function from the socket library to get the IP address for the specified domain
ip_address = socket.gethostbyname(domain)

print(f"The IP address of {domain} is {ip_address}")

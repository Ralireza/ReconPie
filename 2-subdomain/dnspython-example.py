# pip install dnspython
import dns.resolver

domain = "hackerone.com"

# perform a DNS query to get the list of name servers for the domain
ns = dns.resolver.query(domain, 'NS')
# iterate over the name servers and perform a DNS lookup for each of them
for server in ns:
    server = str(server)
    subdomain = "api"
    try:
        answers = dns.resolver.query(subdomain + "." + domain, "A")
        for ip in answers:
            print(subdomain + "." + domain + " - " + str(ip))
    except:
        pass
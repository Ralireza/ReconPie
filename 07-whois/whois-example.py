# pip install python-whois
import whois

domain = 'hackerone.com'

w = whois.whois(domain)

print(w)
# print("Domain registrar:", w.registrar)
# print("WHOIS server:", w.whois_server)
# print("Domain creation date:", w.creation_date)
# print("Domain expiration date:", w.expiration_date)
# print("Domain last updated:", w.last_updated)
# print("Name servers:", w.name_servers)
# print("Registrant name:", w.name)
# print("Registrant organization:", w.org)
# print("Registrant email:", w.email)
# print("Registrant phone:", w.phone)
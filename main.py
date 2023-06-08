
import socket
import os
import dns.resolver
import requests
from bs4 import BeautifulSoup

newpath = r'./data' 
if not os.path.exists(newpath):
    os.makedirs(newpath)


def path():
    print("<-- start check domain and under  -->")
    response = requests.get(url)
    page = BeautifulSoup(response.content, "html.parser")

    links = []
    for link in page.find_all('a'):
        href = link.get('href')          # for links depth 
        if href is not None and href.startswith("http"):
            links.append(href)
    sublinks = []
    for i in links:
        try:
            response = requests.get(i , timeout=0)
        except:
            pass
        page = BeautifulSoup(response.content, "html.parser")
        for link in page.find_all('a'):  # for links depth 2
            href = link.get('href')
            if href is not None and href.startswith("http"):
                sublinks.append(href)

    links.extend(sublinks)
    links = list(dict.fromkeys(links)) #delete tekrary
    original = []
    for link in links:
        if (str(link).find(url[12:]) != -1):
            original.append(link) 

    for i in original:       
        with open('data\\path.txt','a')as path:
            path.writelines(i+os.linesep)

    
    print("<-- finish check domain and under doamins -->")
# 22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
def subdoamin():
    print("<-- start check sub domains -->")
    domain = url[12:]
    ns = dns.resolver.query(domain, 'NS')
    subdomains = []
    with open('wordlist.txt') as txt:
        for line in txt:
            if line.rstrip() != "":
                for server in ns:
                    server = str(server)
                    subdomain = line.rstrip()
                    try:
                        answers = dns.resolver.query(subdomain + "." + domain, "A")
                        for ip in answers:
                            subdomains.append(subdomain + "." + domain)
                    except:
                        pass

    subdomains = list(dict.fromkeys(subdomains))
    with open('data\\subdomain.txt', 'a') as subfile:  # subdomain
        for subdomain in subdomains:
            subfile.write(subdomain + os.linesep)
                            
    print("<-- finish check sub domains -->")
# 333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
def subdomainCodeTitle():
    print("<-- start check status-code sub-domains -->")
    with open('data\\subdomain.txt') as txt:
        for line in txt:
            if line.rstrip() != "":
                try:
                    response = requests.get("https://"+line.rstrip(),timeout=1)
                    page = BeautifulSoup(response.content, "html.parser")
                    try:
                        title = str(page.title.string)
                    except:
                        title = str(page.title)
                except:
                    with open('data\\subdomain+code+title.txt', 'a') as file:  # subdomain+code+ip
                        file.write(line.rstrip() + f' {response.status_code} ' + title + os.linesep)

    print("<-- finish check status-code sub-domains -->")
# 44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
def  subdomainIp():
    print("start check ip sub-domains -->")
    print("writing ips + domains")
    with open('data\\subdomain.txt', 'r') as subdomain:
        for line in subdomain:
            if line.rstrip() != "":
                with open('data\\subdomain+ip.txt', 'a') as file:  # subdomain+ip
                    file.write((line.rstrip() + "    " + socket.gethostbyname(line.rstrip())) + os.linesep)
    print("<-- finish check ip sub-domains -->")
# 55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
def subdomainIpPort():
    print("writing ips + domains + ports -->")
    with open('data\\subdomain.txt', 'r') as subdomain:
        for domain in subdomain:
            ativePort = []
            if domain.rstrip() != "":
                ip = socket.gethostbyname(domain.rstrip())
                common_ports = [21, 22, 23, 25, 53, 80, 110,119, 123, 143, 161, 194, 443, 445, 993, 995]
                for port in common_ports:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)  # Set timeout to 1 second
                    result = sock.connect_ex((ip, port))
                    if result == 0:
                        ativePort = list(dict.fromkeys(ativePort))
                        ativePort.append(port)
                        
                    sock.close()
                with open('data\\subdomain+ip+port.txt', 'a') as ip_port:  # domain+ip+ports
                    ip_port.write(domain.rstrip() + "   " + ip + "   " + str(ativePort) + os.linesep)
    print("<-- finish writing ips + domains + ports -->")
#6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
def subdoaminPhoneEmail():
    print("<-- writing phones + email -->")
    import re
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    with open('data\\subdomain.txt') as subdomain:
        for domain in subdomain:
            emails = []
            phones = []
            if domain.rstrip() != "":
                try:
                    response = requests.get("https://"+domain.rstrip(), verify=False)
                except:
                    pass
                text = str(BeautifulSoup(response.content, "html.parser"))
                # email
                pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
                email = re.search(pattern, text)
                if email:
                    emails.append(email.group())
                # phone number 
                pattern = r"((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))"
                phone = re.search(pattern, text)
                if phone:
                    phones.append(phone.group())
                with open("data\\subdomain+phone+email.txt","a") as adress:
                    adress.write(domain.rstrip() + "   emails" + str(emails) + "  Numbers"  + str(phones) + os.linesep)
#777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
def whoisInfo():
    import whois
    domain = url[12:]
    w = whois.whois(domain)
    with open('data\\moreInformation.txt', 'w') as Whois:
        Whois.writelines(f"""
        Domain registrar:", {str(w.registrar) + os.linesep}
        WHOIS server:", {str(w.whois_server) + os.linesep}
        Domain creation date:", {str(w.creation_date) + os.linesep}
        Domain expiration date:", {str(w.expiration_date) + os.linesep}
        Domain last updated:", {str(w.last_updated) + os.linesep}
        Name servers:", {str(w.name_servers) + os.linesep}
        Registrant name:", {str(w.name) + os.linesep}
        Registrant organization:", {str(w.org) + os.linesep}
        Registrant email:", {str(w.email) + os.linesep}
        Registrant phone:", {str(w.phone) + os.linesep}
        """)
        

import argparse
import os

parser = argparse.ArgumentParser(description='Process some inputs.')
parser.add_argument('--url',required=True, type=str, help='process url')
parser.add_argument('--level',required=True,type=int, help=f"""chose the level: 
1: path , 
2: subdomains , 
3: subdomains+StatusCode+title , 
4: subdomains+ips , 
5: subdomains+ips+ports , 
6: subdomains+phone+email , 
7: whois information
""")
args = parser.parse_args()

if args.url is not None:
    if('www' not in args.url):
        print('enter the url with <www>')
    url = 'https://' + args.url

if(args.level == 1):
    path()
elif(args.level == 2):
    path()
    subdoamin()
elif(args.level == 3):
    path()
    subdoamin()
    subdomainCodeTitle()
elif(args.level == 4):
    path()
    subdoamin()
    subdomainCodeTitle()
    subdomainIp()
elif(args.level == 5):
    path()
    subdoamin()
    subdomainCodeTitle()
    subdomainIp()
    subdomainIpPort()
elif(args.level == 6):
    path()
    subdoamin()
    subdomainCodeTitle()
    subdomainIp()
    subdomainIpPort()
    subdoaminPhoneEmail()
elif(args.level == 7):
    path()
    subdoamin()
    subdomainCodeTitle()
    subdomainIp()
    subdomainIpPort()
    subdoaminPhoneEmail()
    whoisInfo()

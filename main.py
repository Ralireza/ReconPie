import whois
from port_scanner_socket import PortScanner
from saving_data_options import SaveData
from sitemap_bs4 import SiteMap
from nmap_scanner import NmapPortScanner
from regex import RegExValidation
from dns_python import DNSResolver
from html_mining import HtmlMining
from ip_socket import SocketIp

def save_results(results):
    # loop until user exits
    while True:
        print("1 - Save results")
        print("2 - Return to main menu")
        # take user input for saving or exit
        save_choice = input("Enter your choice: ")
            
        if save_choice == "1":
            # call save_results function
            # create a SaveData object
            save = SaveData()

            # get user choice for saving type
            print("1 - Save in txt")
            print("2 - Save in csv")
            print("3 - Save in html")
            save_option = input("Enter save option code to save the results in file: ")

            # use a dictionary to convert user choice to method name
            save_dict = {
                "1": "txt_file",
                "2": "csv_file",
                "3": "html_file"
            }

            # check whether user input is valid or not
            if save_option in save_dict:
                # execute proper method based on user choice
                getattr(save, save_dict[save_option])(results)
                print("Result saved!")
            else:
                print("Invalid choice!")
            
        elif save_choice == "2":
            break
        else:
            print("Invalid choice!")
    

# loop until user exits
while True:
    print("1- Port Scanner")
    print("2- Site Map")
    print("3- Get valid phone - email from text")
    print("4- Get Whois")
    print("5- Get DNS")
    print("6- HTML Mining")
    print("7- Get Domain IP")
    print("0- Exit")
    # take user input
    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            print("1- nmap scanner")
            print("2- socket scanner")
            print("3- return to main menu")
            port_choice = input("Enter your choice : ")
            if port_choice == "1":
                # ask for IP address
                ip = input("Enter IP address: ")
                # create a NmapPortScanner object
                scanner = NmapPortScanner()
                open_ports = scanner.scan_port(ip)
                save_results(open_ports)
            elif port_choice == "2":
                # ask for IP address
                ip = input("Enter IP address: ")
                
                # create a PortScanner object
                scanner = PortScanner()
                open_ports = scanner.get_open_ports(ip)
        
                # print all open ports
                for port in open_ports:
                    print(f"The port {port} is open on IP {ip}")
                
                save_results(open_ports)
            elif port_choice == "3":
                break
            else:
                print("invalid input")
    elif choice == "2":
        # ask for URL and maximum depth
        url = input("Enter URL: ")
        depth = input("Enter maximum depth: ")

        # create a SiteMap object and crawl the URL
        site_map = SiteMap.crawl_site(url, int(depth))
        
        # print the site map
        for page, links in site_map.items():
            print(f"Links on page {page}:")
            for link in links:
                print(f"\t{link}")
        
        save_results(site_map)
    elif choice == "3":
       while True:
            print("1- get all emails from input text")
            print("2- get all phone numbers from input text")
            print("3 - Return to main menu")
            validation_choice = input("Enter your choice: ")
            if validation_choice == "1":
                # ask for text
                filepath = input("Enter text file path: ")
                text = open(filepath).read()
                # create a RegExValidation object
                validation = RegExValidation()
                # get all emails from text
                emails = validation.get_emails(text)
                # print all emails
                for email in emails:
                    print(f"Email: {email}")
                save_results(emails)
                
            elif validation_choice == "2":
                # ask for text
                filepath = input("Enter text file path: ")
                text = open(filepath).read()
                # create a RegExValidation object
                validation = RegExValidation()
                # get all phone numbers from text
                phone_numbers = validation.get_phone_numbers(text)
                # print all phone numbers
                for phone in phone_numbers:
                    print(f"Phone: {phone}")
                save_results(phone_numbers)
        
    elif choice == "4":
       # get whois
       while True:
            print("1- get whois")
            print("2- return to main menu")
            get_whois_choice = input("Enter your choice: ")
            if get_whois_choice == "1":
                # ask for IP address
                domain = input("Enter Domain address: ")
                # get whois
                w = whois.whois(domain)
                # print whois
                print(w)
                save_results(w)
            elif get_whois_choice == "2":
                break
            else:
                print("invalid input")
        
    elif choice == "5":
       # get dns
       while True:
            print("1- get dns")
            print("2- return to main menu")
            get_dns_choice = input("Enter your choice: ")
            if get_dns_choice == "1":
                # ask for Domain address
                domain = input("Enter Domain address: ")
                # get dns
                d = DNSResolver()
                # save dns
                dns_result = d.get_dns(domain)
                save_results(dns_result)
            elif get_dns_choice == "2":
                break
            else:
                print("invalid input")
    elif choice == "6": 
        # HtmlMining : get_title , get_content , get_status , get_links
        while True:
            print("1- get title")
            print("2- get content")
            print("3- get status")
            print("4- get links")
            print("5- return to main menu")
            html_mining_choice = input("Enter your choice: ")
            if html_mining_choice == "1":
                # ask for URL
                url = input("Enter URL: ")
                # create a HtmlMining object
                html_mining = HtmlMining()
                # get title
                title = html_mining.get_title(url)
                # print title
                print(title)
                save_results(title)
            elif html_mining_choice == "2":
                # ask for URL
                url = input("Enter URL: ")
                # create a HtmlMining object
                html_mining = HtmlMining()
                # get content
                content = html_mining.get_content(url)
                # print content
                print(content)
                save_results(content)
            
            elif html_mining_choice == "3":
                # ask for URL
                url = input("Enter URL: ")
                # create a HtmlMining object
                html_mining = HtmlMining()
                # get status
                status = html_mining.get_status(url)
                # print status
                print(status)
                save_results(status)
            elif html_mining_choice == "4":
                # ask for URL
                url = input("Enter URL: ")
                # create a HtmlMining object
                html_mining = HtmlMining()
                # get links
                links = html_mining.get_links(url)
                # print links
                print(links)
                save_results(links)
            elif html_mining_choice == "5":
                break
            else:
                print("invalid input")
    elif choice == "7":
        # get domain ip
        while True:
            print("1- get domain ip")
            print("2- return to main menu")
            get_domain_ip_choice = input("Enter your choice: ")
            if get_domain_ip_choice == "1":
                # ask for Domain address
                domain = input("Enter Domain address: ")
                # create a SocketIP object
                domain_ip = SocketIp()
                # get domain ip
                ip = domain_ip.GetIpFromDomain(domain)
                # print domain ip
                print(ip)
                save_results(ip)
            elif get_domain_ip_choice == "2":
                break
            else:
                print("invalid input")
    elif choice == "0":
       # exit program
       break
    else:
        print("Invalid choice!")
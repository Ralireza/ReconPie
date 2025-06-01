# ReconPie
simple reconnaissance tool project for learning python and basic concepts of programming/networking step by step.

# Features
- Sitemap Generation
- Subdomain Enumeration
- Status Code and Title Retrieval
- Domain to IP Mapping
- Open Ports Scanning
- Regex
- Whois Lookup
- Command-Line Usage with Argparse
- Git
- Reports Generation
- File Enumeration and Download
- Wappalyzer Integration
- Gowitness Integration
- MultiURL Implementation
- History Tracking
- Simple Back-end
- Simple Front-end


# Hall Of Fame

1. Hadi~Killer  : https://github.com/HadiKiler/RECOUN 
2. Mahdi We1rd  : https://github.com/MahdiWe1rd/reconisance 
3. HosseinMohammady  : https://github.com/HosseinMohammady/Reconnaissance-tool
4. Hamed Fakoori  : https://github.com/Hamed-244/Recon
5. Ali Asghar Fathi Khah : https://github.com/aliasgharfathikhah/RECON
6. Seyed MohammadHosein Hamze Jebeli: https://github.com/mmd-coder/ReconPie
7. Hamed amiri sabet :https://github.com/HHKINGHH/RECONE_h
# Steps

## Sitemap Generation
The tool should be capable of list all URLs  for the target website, which will help in discovering all the web pages present on the website. This feature will help identify hidden pages that might not be easily accessible through the website's navigation menu. depth of finding should be 2.
1. Learn basic HTML
2. <a href
3. HTTP request 
4. Request with python
5. Parse html with BeautifulSoup
6. Implement crawler to collect all link in page with depth


## Subdomain Enumeration
Subdomain enumeration is the process of finding subdomains associated with the target website. This feature will help in identifying all the subdomains associated with the target website, which may not be visible through the website's main domain.

1. python read/write files
2. Loop on each lines of file
3. what is IP? 
4. what is DNS?
5. what is Domain?
6. what is subdomain?
7. dnspython
8. Download wordlists
9. Test each word on dns request and collect them
10. try except in python
## Status Code and Title Retrieval
The tool should retrieve the HTTP status codes and titles of all the discovered subdomains. This feature will help in identifying all the web pages that are currently active, and also give an idea of the content present on those pages.
1. HTTP status codes
2. get title of page with BeautifulSoup

## Domain to IP Mapping
The tool should be able to map all subdomains to their corresponding IP addresses. This feature will help in identifying the hosting provider of the target website and any other websites hosted on the same server.
1. OSI model network
2. socket in pyhton
3. subdomains to ip

## Open Ports Scanning
The tool should be able to scan for open ports on the target website. This feature will help in identifying any services running on the website and may reveal potential vulnerabilities.
1. what is server?
2. what is port?
3. common ports
4. socket to check

## Regex
The tool should be capable of extracting emails and phone numbers from all subdomains. This feature will help in identifying contact details of the website's owners or administrators.
1. what is regex?
2. how to use regex in python?
3. regex to find email
4. regex to find phonenumber

## Whois Lookup
The tool should be able to perform a Whois lookup on the target website. This feature will help identify the registration information of the domain, including the owner's name, email address, and registration dates.
1. what is whois?
2. how to check domain whois? 
3. whois in python
## Command-Line Usage with Argparse
The tool should provide command-line usage with argparse, which is a Python module that makes it easy to write user-friendly command-line interfaces.
1. what is args?
2. args in python
3. argparse library


## Git
The project should be added to a GitHub repository, where all the development progress and source code will be stored.
A markdown file should be created in the repository to explain how to use the tool effectively and help new users get started with it.
The developer should also learn how to fork the project and send pull requests to the original repository. This feature is essential for contributing to open-source projects, and it helps acknowledge the developer's contributions as well.

1. what is git?
2. gitlab / github
3. learn git basic commandLine(init, add, commit, push, pull, ...)
4. create repository on github and push your codes
5. fork current repository and make pull request to add your project link to "hall of fame".

## Reports Generation
The tool should be able to generate reports in TXT/CSV/HTML formats. These reports should contain the results of all the tasks performed by the tool, such as sitemap generation, subdomain enumeration, and open port scanning.

1. list all urls
2. list all subdomains with http code and title
3. list all subdomains with ip
4. list all ip with open ports
5. list all email & phonenumber finded
6. save whois 


## File Enumeration and Download
The tool should be able to enumerate files on a target domain and download them. This feature is useful for retrieving sensitive information from the target domain.
 This feature will help in retrieving valuable information present in these files, which may be hidden from regular web pages.

## Wappalyzer Integration
The tool should integrate with Wappalyzer for technology discovery. Wappalyzer is a browser extension that uncovers the technologies used on websites, allowing users to see what software runs under the hood of any website.

## Gowitness Integration
The tool should integrate with Gowitness for taking screenshots of subdomains. Gowitness is an open-source project that enables you to capture screenshots of web pages in batch mode.


## MultiURL Implementation
The tool should implement Multithreading for performing multiple tasks simultaneously. This feature will help save time when dealing with large targets and increase efficiency.

## Simple Back-end
The tool should enable history tracking with Flask and SQLite backend. This feature will allow the user to keep track of all the performed tasks and the results generated by the tool.

## Simple Front-end
The tool should have a simple HTML/CSS/JS frontend that allows users to interact with the tool efficiently. The frontend should provide a user-friendly interface for running scans and generating reports.


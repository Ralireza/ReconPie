# RECOUN
this project is smaple for reconnaissance :<br>
it can scan a website and search about it paths , subdomains , ips , ports<br>
and it can search for emails and phone numbers in subdomains.


this file is a test from ReconPie project **Ralireza**<br>

when you run main.py :<br>
you shoud insert Url this mode after main.py : --url www.Examole.com<br>
after it insert level: --level 1 until 7<br>
chose the level:
1: path <br>
2: subdomains <br>
3: subdomains+StatusCode+title <br>
4: subdomains+ips <br>
5: subdomains+ips+ports <br>
6: subdomains+phone+email <br>
7: whois information <br>

main.py will automatically  creats and write a some files in **data** folder that <br>
Each file is for one level


also you can add subdomains would like for check from **word list full** to **word list**

for run you need to install :<br>
pip install beautifulsoup4<br>
pip install requests<br>
pip install dnspython<br>
pip install python-whois<br>

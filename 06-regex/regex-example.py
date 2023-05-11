import re
# email

text = "Please contact us at info@example.com for further information."

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
# Explanation of the pattern:
# \b - match word boundary
# [A-Za-z0-9._%+-]+ - match one or more characters from the set
# @[A-Za-z0-9.-]+ - match "@" followed by one or more characters from the set
# \.[A-Z|a-z]{2,}\b - match "." followed by two or more alphabetic characters

email = re.search(pattern, text)
if email:
    print(email.group())
else:
    print("No email found")


# phone number 

text = "Please call us at 123-456-7890 for further information."

pattern = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
# Explanation of the pattern:
# \b - match word boundary
# \d{3} - match three digits
# [-.]? - match an optional dash or period character 
# \d{3} - match another three digits
# [-.]? - again match an optional dash or period character
# \d{4} - match four digits

phone = re.search(pattern, text)
if phone:
    print(phone.group())
else:
    print("No phone number found")
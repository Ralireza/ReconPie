import re

class RegExValidation:
    def validate_email(text):
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        # Explanation of the pattern:
        # \b - match word boundary
        # [A-Za-z0-9._%+-]+ - match one or more characters from the set
        # @[A-Za-z0-9.-]+ - match "@" followed by one or more characters from the set
        # \.[A-Z|a-z]{2,}\b - match "." followed by two or more alphabetic characters
        email = re.search(pattern, text)
        if email:
            print(f"Your Email Is Valid! and email group is : {email.group()}")
            return email.group()
        else:
            print("No email found - Email Validation Failed!")
            return []
    def validate_phone_number(text):
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
            print(f"Your Email Is Valid! and email group is : {phone.group()}")
            return phone.group()
        else:
            print("No phone number found - phone number Validation Failed!")
            return []
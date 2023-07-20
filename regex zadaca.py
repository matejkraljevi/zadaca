import re

def provjeri_email(email):
    regex = r'^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$'
    if re.match(regex, email):
        return True
    else:
        return False

def provjeri_eduid(eduid):
    regex = r'^[a-zA-Z]+\.[a-zA-Z]+\d*@sum\.ba$'
    if re.match(regex, eduid):
        return True
    else:
        return False

email = input("Unesite e-mail adresu: ")
if provjeri_email(email):
    print("Uneseni e-mail je validan.")
else:
    print("Uneseni e-mail nije validan.")

eduid = input("Unesite eduId: ")
if provjeri_eduid(eduid):
    print("Uneseni eduId je validan.")
else:
    print("Uneseni eduId nije validan.")

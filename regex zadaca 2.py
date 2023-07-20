import re

string = "Matej Kraljević"
ime = "Matej"
prezime = "Kraljević"

regex = fr"^{ime[0]}.*[0-5].*{prezime[0]}$"

if re.match(regex, string):
    print("Podudaranje pronađeno.")
else:
    print("Podudaranje nije pronađeno."

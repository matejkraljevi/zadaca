import random

imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John',
         'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly',
         'Dan', 'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']
prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles',
             'Perez', 'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt',
             'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

radnici = []
isplate = []

for _ in range(15):
    ime = random.choice(imena)
    prezime = random.choice(prezimena)
    satnica = round(random.uniform(4, 6), 2)
    radnik = {"ime": ime, "prezime": prezime, "satnica": satnica}
    radnici.append(radnik)
    t_sati = random.randint(20, 30)
    radnik["tjedni_sati"] = t_sati
    isplata = round(satnica * t_sati, 2)
    isplate.append((ime, prezime, isplata))

ukupna_isplata = sum(isplata for _, _, isplata in isplate)
prosjecna_isplata = ukupna_isplata / len(isplate)

print("Evidencija radnika:")
for radnik in radnici:
    print(radnik)

print("\nObračun isplata:")
for ime, prezime, isplata in isplate:
    print(f"{ime} {prezime}: {isplata}")

print("\nUkupna isplata za tjedan:", ukupna_isplata)
print("Prosječna isplata za tjedan:", prosjecna_isplata)

print("\nRadnici s isplatom iznad prosjeka:")
for ime, prezime, isplata in isplate:
    if isplata > prosjecna_isplata:
        print(f"{ime} {prezime}")

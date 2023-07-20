import random

imena = ['Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka', 'Antonio', 
         'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David', 'Ivan', 'Petar', 'Marija', 
         'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej', 'Jozo Matej', 'Petar', 'Ivan', 'Stjepan', 
         'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana', 'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan', 
         'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano', 'Mate', 'Mateo', 'Harun']

ocjene = {}

for ime in imena:
    ocjena = random.randint(1, 5)
    if ime in ocjene:
        ocjene[ime].append(ocjena)
    else:
        ocjene[ime] = [ocjena]

brojanje_ocjena = {}

for ocjene_lista in ocjene.values():
    for ocjena in ocjene_lista:
        if ocjena in brojanje_ocjena:
            brojanje_ocjena[ocjena] += 1
        else:
            brojanje_ocjena[ocjena] = 1

broj_ocjena_vece_od_1 = sum(brojanje_ocjena.get(ocjena, 0) for ocjena in range(2, 6))
postotak_prolaznosti = (broj_ocjena_vece_od_1 / len(imena)) * 100

print("Ocjene:")
for ime, ocjena_lista in ocjene.items():
    for i, ocjena in enumerate(ocjena_lista):
        print(f"{ime}-{i+1}: {ocjena}")

print("\nBroj ocjena:")
for ocjena, broj in brojanje_ocjena.items():
    print(f"{ocjena}: {broj}")

print("\nBroj ocjena većih od 1:", broj_ocjena_vece_od_1)
print("Postotak prolaznosti: {:.2f}%".format(postotak_prolaznosti))


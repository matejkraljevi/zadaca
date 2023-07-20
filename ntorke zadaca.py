polozeni_studenti.sort(key=lambda student: student[1])

for student in polozeni_studenti:
    print(f'{student[0]} {student[1]}: {student[2]} bodova')

ocjene = {
    'Nedovoljan': 0,
    'Dovoljan': 0,
    'Dobar': 0,
    'Vrlodobar': 0,
    'Izvrstan': 0
}

for student in polozeni_studenti:
    bodovi = student[2]

    if bodovi >= 0 and bodovi < 50:
        ocjene['Nedovoljan'] += 1
    elif bodovi >= 50 and bodovi < 65:
        ocjene['Dovoljan'] += 1
    elif bodovi >= 65 and bodovi < 80:
        ocjene['Dobar'] += 1
    elif bodovi >= 80 and bodovi < 90:
        ocjene['Vrlodobar'] += 1
    elif bodovi >= 90 and bodovi <= 100:
        ocjene['Izvrstan'] += 1

for ocjena, broj_ocjena in ocjene.items():
    print(f'{ocjena}: {broj_ocjena}')

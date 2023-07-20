def standardna_funkcija(ime):
    return f"Pozdrav {ime}!"

lambda_funkcija = lambda ime: f"Dobrodošao {ime}!"

def poziv_funkcije(funkcija):
    ime = "Frano"
    return funkcija(ime)

print(poziv_funkcije(standardna_funkcija))
print(poziv_funkcije(lambda_funkcija))

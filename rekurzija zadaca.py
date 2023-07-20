
def ispisi_unatrag(string):
    if len(string) == 0:
        return
    else:
        ispisi_unatrag(string[1:])
        print(string[0], end="")

ispisi_unatrag("matej")

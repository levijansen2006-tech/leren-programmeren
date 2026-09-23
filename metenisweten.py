nr1 = int(input("Voer het eerste gehele getal in: "))
nr2 = int(input("Voer het tweede gehele getal in: "))

if nr1 == nr2:
    print(f"Beide getallen zijn even groot (nr1: {nr1}, nr2: {nr2})")

elif nr1 > nr2:
    print(f"nr1 ({nr1}) is groter dan nr2 ({nr2})")

else:
    print(f"nr2 ({nr2}) is groter dan nr1 ({nr1})")

print("Welkom bij de snackautomaat!")
print("Je kunt kiezen uit:")
print("a = Chocoladereep")
print("b = Zakje chips")
print("c = Blikje cola")
print("d = Pakje kauwgom")
print("e = Flesje water")

snacks = input("Wat wil je uit de automaat halen? (bijv. acd): ")

if "a" in snacks:
    print("Je krijgt een chocoladereep.")

if "b" in snacks:
    print("Je krijgt een zakje chips.")

if "c" in snacks:
    print("Je krijgt een blikje cola.")

if "d" in snacks:
    print("Je krijgt een pakje kauwgom.")

if "e" in snacks:
    print("Je krijgt een flesje water.")

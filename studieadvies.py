from studieadviestext import *

print(COMPETENTIE_STELLING_1)
antwoord1 = int(input(OPTIES))

print("Jouw antwoord was:", antwoord1)

print(COMPETENTIE_STELLING_2)
antwoord2 = int(input(OPTIES))

print("Jouw antwoord was:", antwoord2)

print(COMPETENTIE_STELLING_3)
antwoord3 = int(input(OPTIES))

print("Jouw antwoord was:", antwoord3)

print(COMPETENTIE_STELLING_4)
antwoord4 = int(input(OPTIES))

print("Jouw antwoord was:", antwoord4)

print(COMPETENTIE_STELLING_5)
antwoord5 = int(input(OPTIES))

print("Jouw antwoord was:", antwoord5)

print(COMPETENTIE_STELLING_6)
antwoord6 = int(input(OPTIES))

print("Jouw antwoord was:", antwoord6)

print(COMPETENTIE_STELLING_7)
antwoord7 = int(input(OPTIES))

print("Jouw antwoord was:", antwoord7)

eindscore = (antwoord1 + antwoord2 + antwoord3 + antwoord4 + antwoord5 + antwoord6 + antwoord7)/7

if eindscore <= 2:     
    print(COMPETENTIE_ADVIES_ZORGELIJK)
elif eindscore <= 3:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)
    





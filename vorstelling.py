inputNaam = input("Wat is je naam? ")
vraagleeftijd = int(input("Hoe oud ben je? "))
askGender = input("Ben je een A) een jonge of B) een meisje? ").lower()
vraagKleur = input("Wat is je favoriete kleur? ")
vraagGetal = int(input("Wat is je favoriete getal? "))
verschil = abs(vraagleeftijd-vraagGetal)
gender = 'haar' if askGender == 'b' else 'zijn'

print("")
print("Mag ik je voorstellen aan", inputNaam)
print(f"{gender.capitalize()} leeftijd is:", vraagleeftijd)
print(f"{inputNaam}'s favoriete kleur is:", vraagKleur)
print(f"Het verschil tussen {gender} leeftijd en {vraagGetal} is:", verschil)

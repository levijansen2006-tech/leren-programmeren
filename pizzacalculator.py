largePrice =9.50
mediumPrice =8.00
smallPrice =6.50

amountLarge = int(input('hoeveel large pizzas wilt u'))
amountMedium = int(input('hoeveel medium pizzas wilt u'))
amountSmall = int(input('hoeveel small pizzas wilt u'))

totalCostLarge = largePrice * amountLarge
totalCostMedium = mediumPrice * amountMedium
totalcostSmall = smallPrice * amountSmall

total = totalCostLarge + totalCostMedium + totalcostSmall

print('***************kassabon***************')

print(f"pizzalarge {amountLarge}  X    {totalCostLarge}")
print(f"pizzamedium {amountMedium}  X  {totalCostMedium}")
print(f"pizzamesmall {amountSmall}  X  {totalcostSmall}")

print("------------------------------")
print(f"totaal: ${total:.2f}")
print("prijs inclusief btw")

 

kostPP = 7.45
vipVr = 0.37

totalVipCostPP = vipVr*9
totalCostPP = round(totalVipCostPP + kostPP,2)
totalCost = round(totalCostPP*5,2)

totalFor2 = round(totalCost/2,2)

print("Per persoon kost de VIP-VR-gameseat", totalVipCostPP, "euro")
print("per persoon kost het totaal", totalCostPP, "euro")
print("in totaal kost het dus", totalCost, "euro")
print("dit geweldige dagje uit met 5 mensen in de speelhal met 45 minuten VR kost je dus", totalFor2, "euro per persoon voor 2 mensen om te betalen")
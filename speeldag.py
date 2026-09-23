kostPP = 7.45
VipVrKostenPer5Minuten = 0.37
aantalpersonen = 5
tijdvr = 45
betalendePersonen = 2

totalVipCostPP = VipVrKostenPer5Minuten*(tijdvr/5)
totalCostPP = round(totalVipCostPP + kostPP,2)
totalCost = round(totalCostPP*aantalpersonen, 2)

totalFor2 = round(totalCost/betalendePersonen, 2)

print("Per persoon kost de VIP-VR-gameseat", totalVipCostPP, "euro")
print("per persoon kost het totaal", totalCostPP, "euro")
print("in totaal kost het dus", totalCost, "euro")
print(f"dit geweldige dagje uit met {aantalpersonen} mensen in de speelhal met {tijdvr} minuten VR kost je dus", totalFor2, f"euro per persoon voor {betalendePersonen} mensen om te betalen")
# Value Numbers:
Croissant = 0.39
Aantal_Croissant = 17
Stokbrood = 2.78
Aantal_Stokbrood = 2
Totaal_Stokbrood = (Stokbrood*Aantal_Stokbrood)
Totaal_Croissant = (Croissant*Aantal_Croissant)
Totaal = (Totaal_Croissant+Totaal_Stokbrood)
factuurtext = 'De prijs van '+str(Aantal_Croissant) + ' Croisantjes van '+str(Croissant)+' is '+str(Totaal_Croissant)+' en de prijs van '+str(Aantal_Stokbrood)+' Stokbroden van ' + str(Stokbrood)+' is '+str(Totaal_Stokbrood)+' dus het totale bedrag word '+str(Totaal)

print(factuurtext)
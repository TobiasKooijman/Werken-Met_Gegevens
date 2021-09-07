# Variables

Ticket_PP = 7.45
Aantal_Mensen = 4
VIP_Gameseat_Pr5 = 0.37
Tijd_Gameseat = 4
Ticket_totaal = (Ticket_PP*Aantal_Mensen)
Gameseat_Totaal = (VIP_Gameseat_Pr5*Tijd_Gameseat)
Totaal = (Gameseat_Totaal+Ticket_totaal)

# Sommen en Prints en shit

factuurtext = 'De prijs voor '+str(Aantal_Mensen) + ' mensen is per persoon '+str(Ticket_PP)+' is dus '+str(Ticket_totaal)+' totaal en de prijs van een VIP Gameseat is '+str(VIP_Gameseat_Pr5)+' per 5 minuten en de tijd dat we willen is ' + str(Tijd_Gameseat)+' is '+str(Gameseat_Totaal)+' dus het totale bedrag word '+str(Totaal)

print(factuurtext)

def statmenu(statok: dict) -> None:
    if statok["jegy"] == True:
        jegy = "Van"
    else: jegy = "Nincs"
    
    print("\n_______________________________________________________________")
    print(f'\nPénz: {statok["penz"]} Ft\t\t{statok["varos"]}-{statok["idojaras"]}\t\tIdő: {statok["ido"]}')
    print(f'\nKaja: {statok["kaja"]}%\t\tEnergia: {statok["energia"]}%\t\tJegy: {jegy}')
    print(  "_______________________________________________________________")
#inv
# print(f'\nInventory:\nFánk: {inventory["Fánk"]}\t\t\tSportszelet: {inventory["Sportszelet"]}\t\tEnergiaital: {inventory["Energiaital"]}')
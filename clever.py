import os
def startOpties(keuze):
    match keuze:
        case 1:
            return nieuwSpel()
        case 2:
            return spelLijst()
        case 3: 
            return spelers()

def nieuwSpel():
    print("NIEUW SPEL")

def spelLijst():
    print("LIJST SPELLETJES")

def spelers():
    print("SPELERS")
    print("1. Nieuwe speler aanmaken")
    print("2. Spelers bekijken")
    print("3. Terug")
    keuze = int(input())
    os.system('cls')
    spelersOpties(keuze)

def spelersOpties(keuze):
    match keuze:
        case 1:
            return nieuweSpeler()
        case 2:
            return spelerLijst()
        case 3: 
            return main()

def nieuweSpeler():
    print("Voer nieuwe speler in: ")
    file = open("spelersLijst.txt","a")
    file.write(input() + "\n")
    spelerLijst()
    file.close()

def spelerLijst():
    print("1. Terug")
    file = open("spelersLijst.txt", "r")
    print(file.read())
    file.close()
    keuze = int(input())
    if(keuze == 1):
        os.system("cls")
        spelers()
    else:
        spelerLijst()
def main():
    print("1. Nieuw spel invoeren")
    print("2. Spellen bekijken")
    print("3. Spelers")
    keuze = int(input())
    os.system('cls')
    startOpties(keuze)

        
main()

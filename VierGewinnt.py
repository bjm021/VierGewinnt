# Um die Konsole zu clearen (cls oder clear)
from os import system, name


# farben auf der konsole
class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


feld = []
feldSizeX = 0
feldSizeY = 0


def clear():
    # windows
    if name == 'nt':
        _ = system('cls')
        # mac / linux
    else:
        _ = system('clear')
    print(bcolors.ENDC)


def welcome():
    print(bcolors.ENDC)
    print("Willkommen zu VierGewinnt")
    printLogo()
    setSize()


def printLogo():
    print(bcolors.ENDC, end='')
    print("""


____   ____.__                ________              .__               __   
\   \ /   /|__| ___________  /  _____/  ______  _  _|__| ____   _____/  |_ 
 \   Y   / |  |/ __ \_  __ \/   \  ____/ __ \ \/ \/ /  |/    \ /    \   __\\
  \     /  |  \  ___/|  | \/\    \_\  \  ___/\     /|  |   |  \   |  \  |  
   \___/   |__|\___  >__|    \______  /\___  >\/\_/ |__|___|  /___|  /__|  
                   \/               \/     \/               \/     \/      


                    """)


def setSize():
    global feldSizeX
    global feldSizeY
    print()
    print("Welche größe soll das Feld habn?")
    feldSizeX = input("X: ")
    feldSizeY = input("Y: ")
    try:
        int(feldSizeX)
        int(feldSizeY)
    except:
        print("Da ist etwas mit deiner eingabe schiefgelaufen!!! Bitte beachte das alle Eingaben Integer seien sollen!")
        print("Starte eingabe neu!!")
        setSize()
    print(f"Ok das Feld wird also {feldSizeX} x {feldSizeY} groß sein?")
    print("Ist das OK?")
    choice = input("y/n? ")
    if choice.lower() == "y":
        print("OK")
        print()
        clear()
        initListen()
        game()
    else:
        print("Ok dann kannst du es nun korrigieren...")
        setSize()


def initListen():
    global feldSizeX
    global feldSizeY
    global feld
    for x in range(int(feldSizeX)):
        tmpList = []
        for y in range(int(feldSizeY)):
            tmpList.append(0)
        feld.append(tmpList)


def ausgeben():
    global feld
    global feldSizeX
    global feldSizeY
    printLogo()
    # header
    print(bcolors.ORANGE, end='')
    for x in range(int(feldSizeX)):
        print(f"  {x} ", end='')
    print()
    for x in range(int(feldSizeX)):
        print(f"====", end='')
    print("=|")
    for y in range(int(feldSizeY)):
        for x in range(int(feldSizeX)):
            tmpVal = feld[x][y]

            if int(tmpVal) == 0:
                print(f"| {bcolors.CYAN + '-' + bcolors.ENDC} ", end='')
            elif int(tmpVal) == 1:
                print(f"| {bcolors.RED + 'X' + bcolors.ENDC} ", end='')
            elif int(tmpVal) == 2:
                print(f"| {bcolors.BLUE + '0' + bcolors.ENDC} ", end='')

        print(f"|{bcolors.ORANGE}| {y}")


spielerAmZug = 1


# überprüfe eingabe
def checkinput(check):
    try:
        int(check)
    except ValueError:
        print(bcolors.RED + "Das ist keine Zahl!!" + bcolors.ENDC)
        return False

    if int(check) >= int(feldSizeX):
        print(bcolors.RED + "Diese Zeile existiert nicht!" + bcolors.ENDC)
        return False

    if int(check) < 0:
        print(bcolors.RED + "Du Scherzkeks!" + bcolors.ENDC)
        return False



    return True


def game():
    global spielerAmZug
    global feld


    print(f"Spieler {spielerAmZug} am Zug!")
    ausgeben()
    print()
    print(bcolors.GREEN + "Bitte gebe den Index der Spalte ein, in den du einen Stein setzen willst!")
    print()
    nextcolumn = input("Erwarte Zahl: " + bcolors.PURPLE)
    if not checkinput(nextcolumn):
        print(bcolors.RED +  'ERROR!' + bcolors.ENDC)






# SpielStart
welcome()

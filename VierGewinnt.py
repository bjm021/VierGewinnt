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

# Komplettes Feld
feld = []

# Feldgrößen
feldSizeX = 0
feldSizeY = 0

# Konsole löschen
def clear():
    # windows
    if name == 'nt':
        _ = system('cls')
        # mac / linux
    else:
        _ = system('clear')
    print(bcolors.ENDC)

# Startpunkt
def welcome():
    print(bcolors.ENDC)
    print("Willkommen zu VierGewinnt")
    printLogo()
    setSize()

# LOGO ausgeben
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

# Nutzer nach größen Fragen
def setSize():
    global feldSizeX
    global feldSizeY
    print()
    print("Welche größe soll das Feld habn?")
    feldSizeX = input("X: ")
    feldSizeY = input("Y: ")
    # Auf int überprüfen
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
    # y UND Y sollen gehen also alles als LOWER vergleichen
    if choice.lower() == "y":
        print("OK")
        print()
        clear()
        initListen()
        game()
    else:
        print("Ok dann kannst du es nun korrigieren...")
        setSize()

# Listen entsprechend der Größe mit 0 auffüllen
def initListen():
    global feldSizeX
    global feldSizeY
    global feld
    for x in range(int(feldSizeX)):
        tmpList = []
        for y in range(int(feldSizeY)):
            tmpList.append(0)
        feld.append(tmpList)

# haupt ausgeben Methode
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

# Welcher spieler spielt grade? 1 oder 2!!!
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


    print(bcolors.PURPLE + f"Spieler {spielerAmZug} am Zug!" + bcolors.ENDC)
    ausgeben()
    print()
    print(bcolors.GREEN + "Bitte gebe den Index der Spalte ein, in den du einen Stein setzen willst!")
    print()
    nextcolumn = input("Erwarte Zahl: " + bcolors.PURPLE)
    if not checkinput(nextcolumn):
        print(bcolors.RED +  'Drücke Enter um die Eingabe neu zu starten' + bcolors.ENDC)
        input("")
        clear()
        game()
    if not addpiece(nextcolumn):
        print(bcolors.RED + "Zum neu laden der Eingabe Enter drücken..." + bcolors.ENDC)
        input("")
        clear()
        game()


def changePlayer():
    global spielerAmZug

    if int(spielerAmZug) == 1:
        spielerAmZug = 2
    else:
        spielerAmZug = 1


# Füge ein stein einer spalte hinzu
def addpiece(column):
    global feld
    global spielerAmZug
    global feldSizeY

    c = int(column)
    tmpList = feld[c]

    # überprüfe ob Liste voll ist
    if tmpList[0] != 0:
        print(bcolors.RED + "Diese Spalte ist schon voll!" + bcolors.ENDC)
        return False

    #finde letzen leeren index
    #tmpindex = 0
    #print(tmpList)
    #print(len(tmpList))

    index = 0

    for tmpindex in tmpList:
        if tmpindex == 0:
            index = int(index)+1

    tmpList[int(index)-1] = int(spielerAmZug)

    feld[c] = tmpList

    checkWin(int(index)-1, c, int(spielerAmZug))

    changePlayer()
    game()




def checkWin(x, y, player):
    global feld
    global feldSizeX
    global feldSizeY
    # ============================== Vertical ==============================
    tmpVerts = []
    for i in range(x, x+4):
        if int(i) < int(feldSizeY):
            tmpVerts.append(feld[y][i])
        else:
            tmpVerts.append(0)

    # Auswertung
    win = True
    for r in tmpVerts:
        if int(r) != int(player):
            win = False

    #print(tmpVerts)

    # ============================== Horizontal ==============================
    tmpHors = []
    for i in range(y-3, y+4):
        if y < 0:
            tmpHors.append(0)
        if i < int(feldSizeX):
            tmpHors.append(feld[i][x])
        else:
            tmpHors.append(0)

    # Auswertung
    counter = 0
    for r in tmpHors:
        if int(r) == int(player):
            counter = counter + 1
    if int(counter) == 4:
        win = True
    else:
        ein = False

    #print(tmpHors)

    # ============================== Kreuz LO-RU ==============================
    c1 = []
    j = y-3
    for i in range(x-3, x+4):
        if i < 0 or j < 0:
            c1.append(0)
        elif i < int(feldSizeX) and j < int(feldSizeY):
            c1.append(feld[j][i])
        else:
            c1.append(0)

        j = j+1

    # Auswertung
    counter = 0
    for r in c1:
        if int(r) == int(player):
            counter = counter + 1
    if int(counter) == 4:
        win = True
    else:
        ein = False

    #print(c1)

    # ============================== Kreuz LU-RO ==============================

    c2 = []
    j = y+3
    for i in range(x-3, x+4):
        if i < 0 or j < 0:
            c2.append(0)
        elif i < int(feldSizeX) and j < int(feldSizeY):
            c2.append(feld[j][i])
        else:
            c2.append(0)

        j = j-1

    # Auswertung
    counter = 0
    for r in c2:
        if int(r) == int(player):
            counter = counter + 1
    if int(counter) == 4:
        win = True
    else:
        ein = False

    #print(c2)

    if win:
        clear()
        winner(player)


def winner(player):
    if int(player) == 1:
        print(bcolors.BLUE + bcolors.BOLD + """
    
    
    
      _________      .__       .__                  ____    ________              .__               __   
     /   _____/_____ |__| ____ |  |   ___________  /_   |  /  _____/  ______  _  _|__| ____   _____/  |_ 
     \_____  \\\\____ \|  |/ __ \|  | _/ __ \_  __ \  |   | /   \  ____/ __ \ \/ \/ /  |/    \ /    \   __\\
     /        \  |_> >  \  ___/|  |_\  ___/|  | \/  |   | \    \_\  \  ___/\     /|  |   |  \   |  \  |  
    /_______  /   __/|__|\___  >____/\___  >__|     |___|  \______  /\___  >\/\_/ |__|___|  /___|  /__|  
            \/|__|           \/          \/                       \/     \/               \/     \/      
    
    
    
                            """)
        print(bcolors.GREEN + "Herzlichen Glückwunsch Spieler 1" + bcolors.ENDC)
    else:

        print(bcolors.BLUE + bcolors.BOLD + """



            
      _________      .__       .__                 ________     ________              .__               __   
     /   _____/_____ |__| ____ |  |   ___________  \_____  \   /  _____/  ______  _  _|__| ____   _____/  |_ 
     \_____  \\\\____ \|  |/ __ \|  | _/ __ \_  __ \  /  ____/  /   \  ____/ __ \ \/ \/ /  |/    \ /    \   __\\
     /        \  |_> >  \  ___/|  |_\  ___/|  | \/ /       \  \    \_\  \  ___/\     /|  |   |  \   |  \  |  
    /_______  /   __/|__|\___  >____/\___  >__|    \_______ \  \______  /\___  >\/\_/ |__|___|  /___|  /__|  
            \/|__|           \/          \/                \/         \/     \/               \/     \/      
    



                                    """)
        print(bcolors.GREEN + "Herzlichen Glückwunsch Spieler 2" + bcolors.ENDC)

    quit()




# SpielStart
welcome()

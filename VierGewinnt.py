#  ____   ____.__                ________              .__               __
# \   \ /   /|__| ___________  /  _____/  ______  _  _|__| ____   _____/  |_
#  \   Y   / |  |/ __ \_  __ \/   \  ____/ __ \ \/ \/ /  |/    \ /    \   __\
#   \     /  |  \  ___/|  | \/\    \_\  \  ___/\     /|  |   |  \   |  \  |
#    \___/   |__|\___  >__|    \______  /\___  >\/\_/ |__|___|  /___|  /__|
#                    \/               \/     \/               \/     \/
#
#   VierGewinnt
#   by b.jm021 (Benjamin J. Meyer)
#


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
    clear()
    print(bcolors.ENDC)
    print("Willkommen zu VierGewinnt")
    print(bcolors.CYAN + "Erstellt von Benjamin J. Meyer" + bcolors.ENDC)
    printLogo()
    setSize()

# LOGO ausgeben
def printLogo():
    print(bcolors.ENDC, end='')
    print(bcolors.GREEN + """


____   ____.__                ________              .__               __   
\   \ /   /|__| ___________  /  _____/  ______  _  _|__| ____   _____/  |_ 
 \   Y   / |  |/ __ \_  __ \/   \  ____/ __ \ \/ \/ /  |/    \ /    \   __\\
  \     /  |  \  ___/|  | \/\    \_\  \  ___/\     /|  |   |  \   |  \  |  
   \___/   |__|\___  >__|    \______  /\___  >\/\_/ |__|___|  /___|  /__|  
                   \/               \/     \/               \/     \/      


                    """ + bcolors.ORANGE)

# Nutzer nach größen Fragen
def setSize():
    global feldSizeX
    global feldSizeY
    print()
    print("Welche größe soll das Feld habn? Horizontale x Vertikale)")
    feldSizeX = input("X: " + bcolors.PURPLE)
    feldSizeY = input(bcolors.ORANGE + "Y: " + bcolors.PURPLE)
    # Auf int überprüfen
    try:
        int(feldSizeX)
        int(feldSizeY)
    except:
        print(bcolors.RED + "Da ist etwas mit deiner eingabe schiefgelaufen!!! Bitte beachte das alle Eingaben Integer seien sollen!")
        print("Starte eingabe neu!!" + bcolors.ORANGE)
        setSize()

    if int(feldSizeX) < 4 or int(feldSizeY) < 4:
        print(bcolors.RED + "Wenn das Feld kleiner als 4 entweder auf der Horizontalen oder der Vertikalen ist dann kann es keinen Gewinner geben!")
        print("Starte eingabe neu!!" + bcolors.ORANGE)
        setSize()

    print(bcolors.CYAN + f"Ok das Feld wird also {feldSizeX} x {feldSizeY} groß sein?")
    print("Ist das OK?")
    choice = input(bcolors.BLUE + "y/n? " + bcolors.PURPLE)
    # y UND Y sollen gehen also alles als LOWER vergleichen
    if choice.lower() == "y":
        print("OK")
        print()
        clear()
        initListen()
        game()
    else:
        print(bcolors.ORANGE + "Ok dann kannst du es nun korrigieren...")
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

    # header
    print(bcolors.ORANGE + " ", end='')
    for x in range(int(feldSizeX)):
        if int(x)+1 < 10:
            print(f"  {int(x)+1} ", end='')
        else:
            print(f" {int(x) + 1} ", end='')
    print()
    print("|", end='')
    for x in range(int(feldSizeX)):
        print(f"====", end='')
    print("=|")
    for y in range(int(feldSizeY)):
        print(bcolors.ORANGE + "|" + bcolors.ENDC, end='')
        for x in range(int(feldSizeX)):
            tmpVal = feld[x][y]

            if int(tmpVal) == 0:
                print(bcolors.ENDC + f"| {bcolors.CYAN + '-' + bcolors.ENDC} ", end='')
            elif int(tmpVal) == 1:
                print(bcolors.RED + f"| {bcolors.RED + 'X' + bcolors.ENDC} ", end='')
            elif int(tmpVal) == 2:
                print(bcolors.RED + f"| {bcolors.BLUE + '0' + bcolors.ENDC} ", end='')

        print(f"|{bcolors.ORANGE}| {int(y)+1}")

# Welcher spieler spielt grade? 1 oder 2!!!
spielerAmZug = 1


# überprüfe eingabe
def checkinput(check):
    try:
        int(check)
    except ValueError:
        print(bcolors.RED + "Das ist keine Zahl!!" + bcolors.ENDC)
        return False

    if int(check)-1 >= int(feldSizeX):
        print(bcolors.RED + "Diese Zeile existiert nicht!" + bcolors.ENDC)
        return False

    if int(check)-1 < 0:
        print(bcolors.RED + "Du Scherzkeks!" + bcolors.ENDC)
        return False



    return True


def game():
    global spielerAmZug
    global feld


    #print(bcolors.PURPLE + f"Spieler {spielerAmZug} am Zug!" + bcolors.ENDC)
    printLogo()
    ausgeben()
    print()
    print(bcolors.GREEN + "Bitte gebe den Index der Spalte ein, in den du einen Stein setzen willst!")
    print()
    print(bcolors.PURPLE + f"Spieler {spielerAmZug} am Zug!" + bcolors.ENDC)
    print()
    nextcolumn = input("Erwarte Zahl: " + bcolors.PURPLE)
    if not checkinput(nextcolumn):
        print(bcolors.RED +  'Drücke Enter um die Eingabe neu zu starten' + bcolors.ENDC)
        input("")
        clear()
        game()
    checkDraw()
    if not addpiece(int(nextcolumn)-1):
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
    for c in range(0, 7):
        if counter <= 3:
            if tmpHors[c] == player:
                counter = counter+1
            else:
                counter = 0

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
        elif j < int(feldSizeX) and i < int(feldSizeY):
            c1.append(feld[j][i])
        else:
            c1.append(0)

        j = j+1

    # Auswertung
    counter = 0
    for c in range(0, 7):
        if counter <= 3:
            if c1[c] == player:
                counter = counter + 1
            else:
                counter = 0
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
        elif j < int(feldSizeX) and i < int(feldSizeY):
            c2.append(feld[j][i])
        else:
            c2.append(0)

        j = j-1

    # Auswertung
    counter = 0
    for c in range(0, 7):
        if counter <= 3:
            if c2[c] == player:
                counter = counter + 1
            else:
                counter = 0
    if int(counter) == 4:
        win = True
    else:
        ein = False

    #print(c2)

    if win:
        clear()
        winner(player)
    else:
        clear()
        checkDraw()



def checkDraw():
    global feld

    draw = True

    for l in feld:
        if l[0] == 0:
            draw = False

    if draw:
        clear()
        print(bcolors.BLUE + bcolors.BOLD + """
            
     ____ ___                     __                .__    .__           .___             
    |    |   \____   ____   _____/  |_  ______ ____ |  |__ |__| ____   __| _/____   ____  
    |    |   /    \_/ __ \ /    \   __\/  ___// ___\|  |  \|  |/ __ \ / __ |/ __ \ /    \ 
    |    |  /   |  \  ___/|   |  \  |  \___ \\\\  \___|   Y  \  \  ___// /_/ \  ___/|   |  \\
    |______/|___|  /\___  >___|  /__| /____  >\___  >___|  /__|\___  >____ |\___  >___|  /
                 \/     \/     \/          \/     \/     \/        \/     \/    \/     \/ 

        """)
        print(bcolors.RED + "Schade leider unentschieden!" + bcolors.ENDC)
        ausgeben()
        print()
        print()
        print(bcolors.CYAN + "Bitte Enter drücken om das Programm zu beenden!" + bcolors.ENDC)
        input()
        quit()




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



    ausgeben()
    print()
    print()
    print(bcolors.CYAN + "Bitte Enter drücken om das Programm zu beenden!" + bcolors.ENDC)
    input()
    quit()




# SpielStart
welcome()

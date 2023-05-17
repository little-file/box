import os

def fedora():

    def dnfup(x = True):
        while x == True:
            z = input("y/n: ")
            if z   == "n":
                x = False

            if z == "y":
                os.system("#power by little-file")
                os.system("sudo dnf update -y")
                print("done")
                x = False

    def dnfin(x = True):
        while x == True:
            z = input("y/n: ")
            if z == "n":
               x = False
      
            if z == "y":
                c = input("App name: ")
                os.system("sudo dnf in -y "+ c)
                print("done")
                x = False

    def dnfremove(x = True):
        while x == True:
            z = input("y/n: ")
            if z == "n":
                x = False
      
            if z == "y":
                c = input("App name: ")
                os.system("sudo dnf remove -y "+ c)
                print("done")
                x = False

    def dnfsearch(x = True):
        while x == True:
            z = input("y/n: ")
            if z == "n":
                x  = False
      
            if z == "y":
                c = input("App name: ")
                os.system("dnf search "+ c)
                print("done")
                x = False
    x = True

    while x == True:
        print("""    [1]dnf update 
    [2]dnf install
    [3]dnf remove
    [4]dnf search
    [5]quit
    """)
        z = int(input("please number enter: "))
        if z== 1:
            dnfup()
        elif z == 2:
            dnfin()
        elif z == 3:
            dnfremove()
        elif z == 4:
            dnfsearch()
        elif z == 5:
            x = False
def arch():

    def pacmanup(x = True):
        while x == True:
            z = input("y/n: ")
            if z == "n":
                x = False

            if z == "y":
                os.system("sudo pacman -Syu --noconfirm")
                print("done")
                x = False

    def pacmanin(x = True):
        while x == True:
            z = input("y/n: ")
            if z == "n":
               x = False
      
            if z == "y":
                c = input("App name: ")
                os.system("sudo pacman -S --noconfirm "+ c)
                print("done")
                x = False

    def pacmanremove(x = True):
        while x == True:
            z = input("y/n: ")
            if z == "n":
                x = False
      
            if z == "y":
                c = input("App name: ")
                os.system("sudo pacman -Rs "+ c)
                print("done")
                x = False

    def pacmansearch(x = True):
        while x == True:
            z = input("y/n: ")
            if z == "n":
                x = False
      
            if z == "y":
                c = input("App name: ")
                os.system("sudo pacman -Ss "+ c)
                print("done")
                x = False

    x = True

    while x == True:
        print("""    [1]pacman update 
    [2]pacman install
    [3]pacman remove
    [4]pacman search
    [5]quit
    """)
        z = int(input("please number enter: "))
        if z== 1:
            pacmanup()
        elif z == 2:
            pacmanin()
        elif z == 3:
            pacmanremove()
        elif z == 4:
            pacmansearch()
        elif z == 5:
            x = False
def flatpak():

    def flatpakup(x = True):
        while x == True:
            z = input("y/n: ")
            if z == "n":
               x = False
      
            if z == "y":
                os.system("flatpak update -y")
                print("done")
                x = False
    def flatpakin(x = True):
        while x == True:
            z = input("app name: ")
            print("flatpak install -y", z)
            y = input("do you approve ? y/n: ")
            if y == "y":
                os.system("flatpak install -y "+ z)
            if y == "n":
                x = False

    def flatpakremove(x = True):
        while x == True:
            z = input("app name: ")
            print("flatpak remove -y", z)
            y = input("do you approve ? y/n: ")
            if y == "y":
                os.system("flatpak remove -y "+ z)
            if y == "n":
                x = False

    def flatpaksearch(x = True):
        while x == True:
            z = input("app name: ")
            print("flatpak search", z)
            y = input("do you approve ? y/n: ")
            if y == "y":
                os.system("flatpak search "+ z)
            if y == "n":
                x = False
    x = True

    while x == True:
        print("""    [1]flatpak update 
    [2]flatpak install apps
    [3]flatpak remove apps
    [4]flatpak search apps
    [5]quit
    """)
        z = int(input("please number enter: "))
        if z== 1:
            flatpakup()
        if z == 2:
            flatpakin()
        if z == 3:
             flatpakremove()
        if z == 4:
            flatpaksearch()
        elif z == 5:
            x = False

while True:
    print("""
    [1] flatpak
    [2] fedora
    [3] arch
    [4] exit
    """)
    c = int(input("Nuber enter: "))
    if c == 1:
        flatpak()
    elif c == 2 :
        fedora()
        break
    elif c == 3 :
        arch()
        break
    elif c == 4:
        exit()
    else:
        print('false enter')
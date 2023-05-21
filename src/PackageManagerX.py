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
    def pacmancu():
        while True:
            c = input("accept(y) or refuse(n) enter: ")
            if c == 'y':
                os.system("sudo pacman -Sy")
            elif c == 'n':
                break
            else:
                print("False input")
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
        print("""    [1] update 
    [2] install
    [3] remove
    [4] search
    [5] check update
    [6] quit
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
            pacmancu()
        elif z == 6:
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

def ubuntu():
    def usearch():
        while True:
            c = input("app name:")
            os.system("apt search {}".format(c))
    def uinstall():
        while True:
            c = input("app name")
            os.system("sudo apt install -y {}".format(c))
    def uupdate():
        while True:
            c = input("app name")
            os.system("sudo apt update -y " + c)
    while True:
        print("""
        [1] install
        [2] update
        [3] search
        [4] exit""")
        c = int(input("Nuber enter: "))
        if c == 1 :
            uinstall()
        elif c == 2 :
            uupdate()
        elif c == 3:
            usearch()
        elif c == 4:
            exit()
        else:
            print('false enter')
while True:
    print("""
    [1] flatpak
    [2] arch
    [3] fedora
    [4] ubuntu
    [5] exit
    """)
    c = int(input("Nuber enter: "))
    if c == 1:
        flatpak()
    elif c == 3 :
        fedora()
        break
    elif c == 2 :
        arch()
        break
    elif c == 4:
        ubuntu()
    elif c == 5:
        exit()
    else:
        print('false enter')
#I.version
#test version 1x0
import os 
while True:

    print("""
    [1] Games
    [2] Scripts
    [3] Password-ganerade
    [5] funny
    [4] Quit
    [6] sync
    """)
    
    x  = int(input("Number enter: "))
    
    if x == 1:
    
        print("nope")
    
    elif x == 2:
    
        import script
    
        continue

    elif x == 3:

        import password_ganerade

        continue

    elif x == 5:
    
        print("""
    
        I. https://www.chess.com/analysis/game/computer/47503297?tab=analysis
        II.https://www.chess.com/analysis/game/live/71852224971?tab=analysis
        """)
    elif x == 6:
        os.system("sh sync.sh")
    elif x == 4:
    
        break
    
    else:
    
        print("False enter")
    
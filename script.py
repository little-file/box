import os
print("""
[1] dns (only for linux)
[2] PackageManagerX
[3] exit
""")
while True:
    
    c = int(input("Number enter:"))
    
    if c == 1:
        print("write the dns you want(attention We support IPv4)")
        
        n =input(":")
        
        SSID= input("SSID pls enter:")
        
        os.system("nmcli connection modify"+ " '{}' ".format(SSID) +"ipv4.dns" + " '{}'".format(n))
    
    elif c == 2:
    
        import PackageManagerX

        continue
    elif c == 3:
    
        exit()

    else:
    
        print("flase enter")
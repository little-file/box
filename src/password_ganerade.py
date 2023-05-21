import random, os

def classic_password():
    uppercase_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    lowercase_letters = "qazwsxedcrfvtgbyhnujmikol"
    special_characters = "!@#$%^&*()_+-=`~[{]}\;:/?.>,<"
    numbers = "0123456789"

    all_chars = uppercase_letters + lowercase_letters + special_characters + numbers

    length = int(input("Enter password length: "))

    password = "".join(random.sample(all_chars, length))

    print("Your password: ", password)

    accept = input("Do you accept this password? (y/n): ")

    if accept == "n":
        classic_password()

    elif accept == "y":
        ne = input("If you want to write a name or email, write if, if you do not want to write it, write no: ")
        if ne == "n" or "no":
            with open("passwords.txt", "a") as f:
                f.write("password: "+password + "\n")
            return
        with open("passwords.txt", "a") as f:
                f.write("name/email: "+ne+"\n"+"password: "+password + "\n")
                
def unlimited():
    uppercase_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    lowercase_letters = "qazwsxedcrfvtgbyhnujmikol"
    special_characters = "!@#$%^&*()_+-=`~[{]}\|;:/?.>,<"
    numbers = "0123456789"

    all_chars = uppercase_letters + lowercase_letters + special_characters + numbers

    length = int(input("Enter password length: "))

    while True:
        password = "".join(random.sample(all_chars, length))
        print("Your password: ", password)

def read_passwords():
    with open("passwords.txt", "r") as f:
        passwords = f.read()
        print(passwords)

while True:
    print("""    [1] Generate classic password
    [2] Generate unlimited random password
    [3] Read saved passwords
    [4] Quit""")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        classic_password()

    elif choice == 2:
        unlimited()

    elif choice == 3:
        read_passwords()

    elif choice == 4:
        break

    else:
        print("Invalid choice. Please try again.")
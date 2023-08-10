guessed=False

while not guessed:
    password=input("Enter a password:")
    if password == "PhythonCoding":
        guessed=True
        print("Access Granted!")
    else:
        print("acces denied. try again")


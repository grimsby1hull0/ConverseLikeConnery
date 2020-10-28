print("Welcome to Conversh like Connery")


repeat = True

while repeat:
    usertext = input("Enter what you want to be converted into Connery:")

    result = usertext.replace("s","sh")
    result = result.replace("S","Sh")
    print(result)

    yesno = input("Do you wish to quit? (Yes/No):")
    if yesno == "no":
        repeat = True

    if yesno == "No":
        repeat = True

    if yesno == "Yes":
        repeat = False

    if yesno == "yes":
        repeat = False

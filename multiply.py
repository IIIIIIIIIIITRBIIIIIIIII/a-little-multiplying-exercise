x = float(input("enter a number "))
is_running = True

while is_running:
    for i in range(0,11):
        s = x * i
        print(f"{x} x {i} = {s}")

    quit = input("do you want to try an another number (y/n)")

    if quit.lower() == "y":
        x = float(input("enter a number "))
    elif quit.lower() == "n":
        print("you quit")
        is_running = False
    else:
        print("invalide answer")
        quit = input("do you want to try an another number (y/n)")
while True:
    name = input()
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    elif name == "Voldemort":
        print("You must not speak of that name!")
        break
    else:
        length_of_name = len(name)
        if length_of_name < 5:
            print(f"{name} goes to Gryffindor.")
        elif length_of_name == 5:
            print(f"{name} goes to Slytherin.")
        elif length_of_name == 6:
            print(f"{name} goes to Ravenclaw.")
        else:   # elif length_of_name > 6:
            print(f"{name} goes to Hufflepuff.")

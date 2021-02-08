"""A program to demonstrate conditional if-then statements."""

how_much=int=int(input("Pick a number between 0-100: "))

if how_much < 25:
    print("I love you a teensy bit")
else: 
    if how_much < 50:
        print("I love you.")
    else: 
        if how_much < 75:
            print("I really love you.")
        else:
            print("ILYSM!!!")

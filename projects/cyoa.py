"""Create your own aventure."""

from random import randint

__author__ = "730397626"

count: int = 0
odd_number: int = (randint(1,3) * 2 + 1)
even_number: int = (randint(1,3) * 2)
player: str = input("Enter name of player- " )
points: str = (f"Your score is {count}")
i: int = 0
iterations: int = 3
cowboy: str = "\U0001F920"

def greet() -> None:
    """Greeting."""
    greet: str = "welcome to the game" + str(cowboy) +"."
    print(str(player) + ", " + str(greet))
    rules: str = "To win the game, guess the right number."
    print(rules)


def main() -> None:
    """Entrypoint of progsram."""
    greet()
    will_you_play: str = input("Do you wish to continue? Yes or no?- " )
    if will_you_play == str("yes"):
        print("Good Luck!")
    if will_you_play == str("no"):
        print("Goodbye!")
        return None
    choice: str = input("Make a choice. Odd or even?- ")
    if choice == str("odd"):
        odd_game(odd_number)
    if choice == str("even"):
        even_game(even_number)
    main()
    return None

def cont() -> None:
    will_you_keep_play: str = input("Do you wish to continue playing? Yes or no?- " )
    if will_you_keep_play == str("yes"):
        print("You can do it!")
    if will_you_keep_play == str("no"):
        print("Goodbye " + str(plater) + "! Your final score was {count}!!")
        return None

def odd_game(odd_number: int) -> int:
    """Guess an odd number game."""
    guess: int = input("Guess a number 3, 5, or 7 -  ")
    if guess == int(randint(1,3) * 2 + 1):
        count += 1
        print(str(player) + ", that was correct!!") 
        print(str(points))
    else:
        print(str(player) + ", that was incorrect.") 
        print(str(points))
    while i < iterations:
        odd_game(count)
        i += 1
    return count

def even_game(even_number: int) -> int:
    """Guess an even number game."""
    guess: int = input("Guess a number 2, 4, or 6 -  ")
    if guess == (randint(1,3) * 2):
        count += 1
        print(str(player) + ", that was correct!!") 
        print(str(points))
    else: 
        print(str(player) + ", that was incorrect.") 
        print(str(points))
        guess: int = input("Guess a number 2, 4, or 6 -  ")
    while i < iterations:
        even_game(count)
        i += 1
    return count

if __name__ == "__main__":
    main()
"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730397626"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """The fortune cookie portion of the program that returns a str value."""
    number = (randint(1, 4))
    if number <= 2:
        if number != 1:
            w: str = str("Tomorrow will be your lucky day!")
            return w
        else:
            x: str = str("If you can dream it, you can beccome it!")
            return x
    else: 
        if number == 3:
            y: str = str("Happiness ahead!")
            return y
        else:
            z: str = str("Be the change you want to see in the world!")
            return z
    
    
# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()

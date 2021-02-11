"""Tar Heels exercise redux as a structured program."""

__author__ = "730397626"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(integer: int) -> str:
    """The Carolina Tar Heels portion of the program."""
    if integer % 2 == 0 and integer % 7 == 0:
        w: str = str("TAR HEELS")
        return w
    else:
        if integer % 2 == 0:
            x: str = str("TAR")
            return x
        else:
            if integer % 7 == 0:
                y: str = str("HEELS")
                return y
            else:
                z: str = str("CAROLINA")
                return z


if __name__ == "__main__":
    main()

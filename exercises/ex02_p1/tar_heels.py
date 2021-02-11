"""Tar Heels exercise redux as a structured program."""

__author__ = "YOUR 9-DIGIT PID"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(integer: int) -> str:
    if integer % 2 == 0 and integer % 7 == 0:
        x: str = str("TAR HEELS")
    else:
        if integer % 2 == 0:
            x: str = str("TAR")
        else:
            if integer % 7 == 0:
                x: str = str("HEELS")
            else:
                x: str = str("CAROLINA")
    return x


if __name__ == "__main__":
    main()

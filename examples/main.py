"""An idiomatic, Python program."""

def main() -> None:
    """Entrypoint of program."""
    x: int = 2
    print(g(f(x)))
    return None

def g(x: int) -> int:
    """Another silly function."""
    print("g of " + str(x))
    return x * 2

def f(x: int) -> int:
    """A silly, lil function."""
    print("f of " + str(x))
    y: int = x * 2
    return g(y)


if __name__ == "__main__":
    main()
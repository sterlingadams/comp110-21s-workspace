"""Jump around!"""


def yes_no(b: bool) --> str:
    """Converts a bool 'yes' or 'no'."""
    print("JUMP UP!")
    if b:
        return "YES"
    return "NO"
    print("GET DOWN")


def diddukewin(unc: int, duke: int) --> str:
    """Implementation of diddukewin.com."""
    print("JUMP UP?")
    duke = duke - unc
    won: str = yes_no(duke > 0)
    print("JUMP AROUND")
    return won


duke: int = 87
unc: int = 91
print(diddukewin(unc, duke))
 

"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730397626"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    x: int = (days_to_target(population, doses, doses_per_day, target))
    y: str = str(future_date(x))
    print("we will reach " + str(target) + "% vaccination in " + str(x) + " days, which falls on " + str(y) + ".")


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """A function describing the number of days needed to get target vaccinated."""
    target_float: float = float(target) / 100
    total_doses: float = ((2 * population) * target_float)
    doses_left: int = round(total_doses - doses)
    days: int = round(doses_left / doses_per_day)
    return days


def future_date(future: int) -> str:
    """A function describing the projected date the vaccination goal will be reached."""
    date: datetime = datetime.today() + timedelta(future)
    future_date: str = date.strftime("%B %d, %Y")
    return future_date


if __name__ == "__main__":
    main()

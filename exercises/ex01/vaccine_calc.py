"""A vaccination calculator."""

__author__ = "730397626"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime
from datetime import timedelta


population: int = int(input("Population: "))
doses_administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target: str = (input("Target percent vaccinated: "))
target_percentage_float: float = float(target) / 100

total_doses_administered: float = ((2 * population) * target_percentage_float)
doses: int = total_doses_administered - doses_administered
left_to_be_cured: int = round(doses / doses_per_day)

date: datetime = datetime.today() + timedelta(left_to_be_cured)
future_d: str = date.strftime("%B %d, %Y")


print("we will reach " + target + "% vaccination in " + str(left_to_be_cured) + ", days which falls on " + future_d + ".")
"""A vaccination calculator."""

__author__ = "730397626"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


population: int = int(input("Population: "))
doses_administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target_percentage_str: str = (input("Target percent vaccinated: "))
target_percentage_float: float = float(target_percentage_str) / 100

total_doses_administered: float = ((2 * population) * target_percentage_float)
doses: float = total_doses_administered - doses_administered
left_to_be_cured: int = round(doses / doses_per_day)
left_to_be_cured_timedelta: timedelta = timedelta(left_to_be_cured)
today: datetime = datetime.today()
future: datetime = today + (left_to_be_cured_timedelta)
days_str: str = str(left_to_be_cured_timedelta)
future_date: str = future.strftime("%B %d, %Y")
print("we will reach " + target_percentage_str + "% vaccination in " + days_str + " days which falls on " + future_date + ".")
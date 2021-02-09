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


population:int=int(input("Population: "))
doses_administered:int=int(input("Doses administered: "))
doses_per_day:int=int(input("Doses per day: "))
target_percentage_str:str=(input("Target percent vaccinated: "))
target_percentage_float: float = float(target_percentage_str)

left_to_be_cured=round(float((population)-(0.5*doses_administered)))
print(left_to_be_cured)

target_percent_over_population= round(float((100*target_percentage_float)/population))
print(target_percent_over_population)

days: int = (round(float(2.0*(left_to_be_cured-target_percent_over_population))/doses_per_day)

days_converted: timedelta = timedelta(days)
today: datetime = datetime.today()
future: datetime = today + days_converted
days_str: str = str(days)
print("we will reach " + target_percentage_str + "% vaccination in " + days_str + " days which falls on" + future.strftime("%B %d, %Y") +".")

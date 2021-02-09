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
target_percentage:int=int(input("Target percent vaccinated: "))

left_to_be_cured: float = population-((0.5)doses_administered)

days= ((2*(population)/doses_per_day)-(doses_administered/doses_per_day)-((50*(target_percentage))/((population)(doses_per_day))))
print(days)


today: datetime = datetime.today()
future: datetime = today + days
print(future.strftime("%B %d, %Y"))




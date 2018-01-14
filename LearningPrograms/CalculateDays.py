import time
from datetime import date
today = date.today()
print(today)
lwd = date(2018, 1, 29)
pen_days = lwd - today
print("Remaining days : ", pen_days)
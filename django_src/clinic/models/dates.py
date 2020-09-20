import datetime
from django.db import models


# Shall be a configurable table in future implementations
class Timeslot(datetime.time, models.Choices):
	H0800 = (8, 0, 0)
	H0830 = (8, 30, 0)
	H0900 = (9, 0, 0)
	H0930 = (9, 30, 0)
	H1000 = (10, 0, 0)
	H1030 = (10, 30, 0)
	H1100 = (11, 0, 0)
	H1130 = (11, 30, 0)
	H1200 = (12, 0, 0)
	H1230 = (12, 30, 0)
	H1300 = (13, 0, 0)
	H1330 = (13, 30, 0)
	H1400 = (14, 0, 0)
	H1430 = (14, 30, 0)
	H1500 = (15, 0, 0)
	H1530 = (15, 30, 0)
	H1600 = (16, 0, 0)
	H1630 = (16, 30, 0)
	H1700 = (17, 0, 0)
	H1730 = (17, 30, 0)
	H1800 = (18, 0, 0)
	H1830 = (18, 30, 0)
	H1900 = (19, 0, 0)
	H1930 = (19, 30, 0)
	H2000 = (20, 0, 0)
	H2030 = (20, 30, 0)


class Date(models.Model):
	day = models.DateField()
	timeslot = models.TimeField(choices=Timeslot.choices)


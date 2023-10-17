from ActivitiesOrganizer.ChargeActivities.mainCharge import *
from ActivitiesOrganizer.Methods.mainMethods import *
from ActivitiesOrganizer.PrintActivities.mainWrite import *


def test():
#    activities = mainCharge()

    week=chargeWeek([Activity('Gym',4,2,'morning')])

    writeWeek(week)

test()
from ActivitiesOrganizer.ChargeActivities.mainCharge import *
from ActivitiesOrganizer.Methods.mainMethods import *
from ActivitiesOrganizer.PrintActivities.mainWrite import *


def test():
    activities = mainCharge()

    week=chargeWeek(activities)

    writeWeek(week)

test()
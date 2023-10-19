from ActivitiesOrganizer.ChargeActivities.mainCharge import *
from Methods.mainMethods import *
from PrintActivities.mainWrite import *


def test():
#    activities = mainCharge()

    week=chargeWeek([Activity('Gym',2,3,'morning'),Activity('University',2,3,'morning')])

    writeWeek(week)

test()
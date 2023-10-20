#from ActivitiesOrganizer.ChargeActivities.mainCharge import *
from Prototypes.prototypes import Activity
from Methods.mainMethods import *
from PrintActivities.mainWrite import *



def test():
    exampleAct = [Activity('Gym',2,3,'morning'),Activity('University',2,3,'morning'),Activity('Football',2,3,'afterNoon'),Activity('Exam',1,2,'morning'),Activity('Meet',1,4,'afterNoon')]
    #activities = mainCharge()

    week=chargeWeek(exampleAct)

    writeWeek(week)

test()
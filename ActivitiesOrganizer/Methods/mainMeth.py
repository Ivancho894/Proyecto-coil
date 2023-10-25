from Prototypes.prototypes import *


def checkHability(week,act):
    day=week[act.day]
    for i in range(act.hours):
        if(day.activities[act.hour+i-8]!='nothing'):
            return False
    return True

def chargeActByHour(week,act):
    day = week[act.day]
    if(checkHability(week,act)):
        for i in range(act.hours):
            day.activities[act.hour+i-8] = act.name
        week[act.day] = day
        error='none'
    else:
        error = 'No hay tiempo para guardar esa actividad'
    return week,error
from Prototypes.prototypes import *


def removeActByHour(day,hour,dayNum):
    hours=0
    name=day.activities[hour]
        
    while(day.activities!='nothing' and day.activities[hour+hours]==name):
        day.activities[hour+hours]='nothing'
        hours+=1
    return day,Activity(name,hours,hour,dayNum)

def checkHability(week,act):
    day=week[act.day]
    print(act.hour)
    for i in range(act.hours):
        if(day.activities[act.hour+i]!='nothing'):
            return False
    return True

def chargeActByHour(week,act):
    day = week[act.day]
    if(checkHability(week,act)):
        for i in range(act.hours):
            day.activities[act.hour+i] = act.name
        week[act.day] = day
        error='none'
    else:
        error = 'No hay tiempo para guardar esa actividad'
    return week,error

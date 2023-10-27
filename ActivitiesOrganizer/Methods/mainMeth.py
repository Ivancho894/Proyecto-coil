from Prototypes.prototypes import *
from PrintActivities.mainWrite import *

def createWeek():
    week=[]
    for i in range(5):
        week.append(Day())
    return week
def removeActByHour(day,hour,dayNum):
    hours=0
    name=day.activities[hour]
    if(hour-1>-1 and day.activities[hour-1]==name):
        #Si el usuario ingreso la hora despues que haya arrancado
        return removeActByHour(day,hour-1,dayNum)
    while(hour+hours<10 and day.activities[hour+hours]==name ):
        day.activities[hour+hours]='nothing'
        hours+=1
    return day,Activity(name,hours,hour,dayNum)

def checkHability(week,act):
    day=week[act.day]
    for i in range(act.hours):
        if(act.hour+i>9):
            return act.name+' se pasa de las 18 por '+str(act.hours-i)+' horas.'
        if(day.activities[act.hour+i]!='nothing'):
            return 'A las '+str(act.hour+i+8)+' tenes '+str(day.activities[act.hour+i])+'.'

    return 'none'

def chargeActByHour(week,act):
    day = week[act.day]
    error =checkHability(week,act)
    if(error=='none'):
        for i in range(act.hours):
            day.activities[act.hour+i] = act.name
        week[act.day] = day
        
    return week,error

from PrintActivities.mainWrite import *
from ChargeActivities.chargeByHour import *
from Methods.mainMeth import *
import os
def actChoose(week):
    choosed = False


    while(not choosed):
        os.system('clear')
        print('MODIFICACION DE ACTIVIDAD')
        print('Este es su calendario hasta ahora: ')
        writeWeek(week)
        day=dayInput()
        os.system('clear')
        print('Estas son las actividades de ese dia: ')
        printAllHours()
        writeDay(week[day],day)
        startHour = hourInput()
        if(week[day].activities[startHour]!='nothing'):
            choosed=True
        else:
            print('No hay actividades a esa hora')

    
    return day,startHour

def removeAct(week):
    day,startHour= actChoose(week)
    week[day],act = removeActByHour(week[day],startHour,day)
    return week,act

def changeAct(week):
    week,act=removeAct(week)
    return changeSomething(week,act)
    
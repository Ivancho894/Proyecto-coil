from Prototypes.prototypes import Activity
from PrintActivities.mainWrite import *
from ChargeActivities.chargeByHour import *


def createWeek():
    week=[]
    for i in range(5):
        week.append(Day())
    return week

def test():
    op=-1
    week=createWeek()
    while(op!=0):
        print('Este es su calendario hasta ahora: ')
        writeWeek(week)
        print('Menu Principal')
        print('1. Desea cargar actividad')
        print('2. Desea modificar actividad')
        print('0. Salir')
        op=int(input())
        if(op==1):
            week = activityCharge(week)
        
        

test()
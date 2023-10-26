from Prototypes.prototypes import Activity
from PrintActivities.mainWrite import *
from ChargeActivities.chargeByHour import *
from ChargeActivities.chargeByCharge import *
from Methods.mainMeth import *
import os
import time


def createWeek():
    week=[]
    for i in range(5):
        week.append(Day())
    return week

def test():
    op=-1
    week=createWeek()
    week,error=chargeActByHour(week,Activity('Gym',3,1,1))
    while(op!=0):
        # os.system('clear')
        print("BIENVENIDO A SU CALENDARIO \n")
        print('Este es su calendario hasta ahora: ')
        writeWeek(week)
        print('Menu Principal')
        print('1. Desea cargar actividad')
        print('2. Desea modificar actividad')
        print('3. Desea eliminar actividad')
        print('0. Salir')
        try:
            op=int(input('Su opcion: '))
        except ValueError:
            print('Solo numeros permitidos')
            time.sleep(1)
            continue
        if(op==1):
            week = activityCharge(week)
        if(op==2):
            week = changeAct(week)
        if(op==3):
            week,act = removeAct(week)
        
        

test()
from Prototypes.prototypes import *
from Methods.mainMeth import *
from PrintActivities.mainWrite import *

def changeAct(what,week,act):
    if(what==1):
        day = input('Que dia deea hacer la actividad: (lunes = 1 y viernes = 5): ')
        act.day = day
        afterCharge(week,act)    
    if(what==2):
        hours = input('Cuantas horas va a durar: ')
        act.hours = hours
        afterCharge(week,act)
    if(what==3):
        hours = input('A que hora desea hacer la actividad: ')
        act.hours = hours
        afterCharge(week,act)
    

def afterCharge(week,act):
    week,error = chargeActByHour(week,act)
    if(error!='none'):
        #No se cargo correctamente
        print(error)
        print('1. Cambiar dia')
        print('2. Cambiar duracion')
        print('3. Cambiar hora')
        what= int(input('Ingrese una opcion: '))
        changeAct(what,week,act)
    print('Se cargo de forma correcta su actividad')
    return week

    
def activityCharge(week):
    day=int(input('Que dia va ser la actividad: '))
    print('Estas son las actividades de ese dia: ')
    print("{:<8}".format('Hours: ')+printHours(8))
    print('Day ',day,' ',writeDay(week[day-1],0))
    name=input('Como se va a llamar la actividad: ')
    hour=int(input('A que hora desea que comience la actividad: '))
    hours=int(input('Cuantas horas va a durar: '))
    act=Activity(name,hours,hour,day-1)
    return afterCharge(week,act)
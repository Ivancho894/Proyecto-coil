from Prototypes.prototypes import *
from Methods.mainMeth import *
from PrintActivities.mainWrite import *
import os

def dayInput():
    dayCheck=True
    while(dayCheck):
        print(printDays(0))
        day=input('Ingrese el numero de dia que va a ser la actividad: ')
        try:
            day=int(day)
        except ValueError:
            print('Solo numeros permitidos')
            continue
        if(day<1 or day>5):
            print('Los dias son entre 1 y 5')
        else:
            dayCheck=False
    return day-1

def hourInput():
    hourCheck=True
    while(hourCheck):
        try:
            hour=int(input('A que hora es su actividad: '))
        except ValueError:
            print('Solo numeros permitidos')
            continue
        if(hour<8 or hour>17):
            print('Los horas son entre 8 y 17')
        else:
            hourCheck=False
    return hour-8

def hoursInput():
    hoursCheck= True
    while(hoursCheck):
        try:
            hours=int(input('Cuantas horas va a durar: '))
        except ValueError:
            print('Solo numeros permitidos')
            continue
        if(hours<0 or hours>10):
            print('Las horas tienen que ser mayor a 0 y menor a 10')
        else:
            hoursCheck=False
    return hours


def changeSomething(week,act):
    print('Podes cambiar lo siguiente de '+act.name+':')
    print('1. Cambiar dia')
    print('2. Cambiar duracion')
    print('3. Cambiar hora')  
    
    op=int(input('Ingrese una opcion: '))

    week=changeAct(op,week,act)

    return week



def afterCharge(week,act):
    week,error = chargeActByHour(week,act)
    if(error!='none'):
        #No se cargo correctamente
        os.system('clear')
        print('AGREGANDO ',act.name,' A TU CALENDARIO')
        print('Estas son las actividades de ese dia: ')
        printAllHours()
        writeDay(week[act.day],act.day)

        print(error)
        week=changeSomething(week,act)

    return week

def changeAct(what,week,act):
    if(what==1):
        day = dayInput()
        act.day = day
        week=afterCharge(week,act)
    if(what==2):
        hours = hoursInput()
        act.hours = hours
        week=afterCharge(week,act)
    if(what==3):
        hour = hourInput()
        act.hour = hour
        week=afterCharge(week,act)
    return week
    

def activityCharge(week):
    os.system('clear')
    print('AGREGANDO NUEVA ACTIVIDAD')
    day=dayInput()
    os.system('clear')
    print('AGREGANDO NUEVA ACTIVIDAD')
    print('Estas son las actividades de ese dia: ')
    printAllHours()
    writeDay(week[day],day)

    name=input('Como se va a llamar la actividad: ')
    os.system('clear')
    print('AGREGANDO ',name,' A TU CALENDARIO')
    print('Estas son las actividades de ese dia: ')
    printAllHours()
    writeDay(week[day],day)
    hour=hourInput()

    hours=hoursInput()

    act=Activity(name,hours,hour,day)
    return afterCharge(week,act)

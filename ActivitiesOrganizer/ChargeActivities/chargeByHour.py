from Prototypes.prototypes import *
from Methods.mainMeth import *
from PrintActivities.mainWrite import *

def dayInput():
    dayCheck=True
    while(dayCheck):
        day=int(input('Que dia va ser la actividad: '))
        if(day<1 or day>5):
            print('Los dias son entre 1 y 5')
        else:
            dayCheck=False
    return day-1

def hourInput():
    hourCheck=True
    while(hourCheck):
        hour=int(input('A que hora comienza su actividad: '))
        if(hour<8 or hour>17):
            print('Los horas son entre 8 y 17')
        else:
            hourCheck=False
    return hour-8

def hoursInput():
    hoursCheck= True
    while(hoursCheck):
        hours=int(input('Cuantas horas va a durar: '))
        if(hours<0 or hours>10):
            print('Las horas tienen que ser mayor a 0 y menor a 10')
        else:
            hoursCheck=False
    return hours


def changeSomething(week,act):
    
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
        print(error)
        week=changeSomething(week,act)

    print('Se cargo de forma correcta su actividad')
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

    day=dayInput()

    print('Estas son las actividades de ese dia: ')
    print("{:<8}".format('Hours: ')+printHours(8))
    print('Day ',day+1,' ',writeDay(week[day],0))

    name=input('Como se va a llamar la actividad: ')

    hour=hourInput()

    hours=hoursInput()

    act=Activity(name,hours,hour,day)
    return afterCharge(week,act)

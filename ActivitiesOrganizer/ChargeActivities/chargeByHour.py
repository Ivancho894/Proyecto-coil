from Prototypes.prototypes import *
from Methods.mainMeth import *
from PrintActivities.mainWrite import *

def day():
    dayCheck=True
    while(dayCheck):
        day=int(input('Que dia va ser la actividad: '))
        if(day<1 or day>5):
            print('Los dias son entre 1 y 5')
        else:
            dayCheck=False
    return day

def hour():
    hourCheck=True
    while(hourCheck):
        hour=int(input('A que hora desea que comience la actividad: '))
        if(hour<8 or hour>17):
            print('Los horas son entre 8 y 17')
        else:
            hourCheck=False
    return hour

def hours():
    hoursCheck= True
    while(hoursCheck):
        hours=int(input('Cuantas horas va a durar: '))
        if(hours<0 or hours>10):
            print('Las horas tienen que ser mayor a 0 y menor a 10')
        else:
            hoursCheck=False
    return hours

def changeAct(what,week,act):
    if(what==1):
        day = day()
        act.day = day
        afterCharge(week,act)
    if(what==2):
        hours = hours()
        act.hours = hours
        afterCharge(week,act)
    if(what==3):
        hour = hour()
        act.hour = hour
        afterCharge(week,act)
    return week

def changeSothing(week,act):
    
    print('1. Cambiar dia')
    print('2. Cambiar duracion')
    print('3. Cambiar hora')  
    
    op=int(input('Ingrese una opcion: '))

    changeAct(op,week,act)

#FALTA VER LOS RETURN 


def afterCharge(week,act):
    week,error = chargeActByHour(week,act)
    if(error!='none'):
        #No se cargo correctamente
        print(error)
        week=changeSothing(week,act)

    print('Se cargo de forma correcta su actividad')
    return week

    
def activityCharge(week):

    day=day()

    print('Estas son las actividades de ese dia: ')
    print("{:<8}".format('Hours: ')+printHours(8))
    print('Day ',day,' ',writeDay(week[day-1],0))

    name=input('Como se va a llamar la actividad: ')

    hour=hour()

    hours=hours()

    act=Activity(name,hours,hour,day-1)
    return afterCharge(week,act)
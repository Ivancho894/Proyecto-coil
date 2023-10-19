from ActivitiesOrganizer.Prototypes.prototypes import *
import random




def chargeMorning(day,act):
    #Hora en la que empieza la actividad
    startsAt = day.freeTime(act.shift,True)
    for i in range(act.hours):
        #Agrego el nombre de la actividad
        day.morning[startsAt]=act.name
        startsAt+=1
    return day

def chargeAfternoon(day,act):
    #Hora en la que empieza la actividad
    startsAt = day.freeTime(act.shift,True)
    for i in range(act.hours):
        #Agrego el nombre de la actividad
        day.afterNoon[startsAt]=act.name
        startsAt+=1
    return day


def chargeDay(week,act):
    #si tiene tiempo para la actividad lo carga si no se ejecuta recursivamente

    #Elijo un dia random de la semana
    dayNum= random.randint(0,4)

    #Funcion que devuelve cantidad de horas que no hay actividades
    timeLeft=week[dayNum].freeTime(act.shift,False)

    #Devuelve True o False si tiene tiempo para la actividad
    hasTime = timeLeft>=act.hours

    #Funcion de la clase day que chequea si fue la primera vez
    firstTime = week[dayNum].firstTimeCheck(act)

    if (hasTime & firstTime):

        if (act.shift == 'morning'):
            #agrego actividad a la mañana y devuelvo un dia
            week[dayNum]=chargeMorning(week[dayNum],act)
        else:
            #agrego actividad a la tarde y devuelvo un dia
            week[dayNum]=chargeAfternoon(week[dayNum],act)

        if act.days > 1:
            act.days-=1
            chargeDay(week,act)
    else:
       chargeDay(week,act)
    return week,act


def chargeWeek(actVec):
    #creo la semana
    week=[]
    for i in range(5):
        week.append(Day())

    #itero en la cantida de actividaddes para cargarlas en dias
    for i in range(len(actVec)):
        week,actVec[i]=chargeDay(week,actVec[i])
    return week



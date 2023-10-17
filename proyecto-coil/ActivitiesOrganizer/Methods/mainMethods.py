from ActivitiesOrganizer.Prototypes.prototypes import *
import random

def chargeDay(week,act):
    #si tiene tiempo para la actividad lo carga si no se ejecuta recursivamente

    #Elijo un dia random de la semana
    dayNum= random.randint(1,5)

    #Devuelve True o False si tiene tiempo para la actividad
    hasTime = week[dayNum].hoursLeft(act.shift)>=act.hours
    #Funcion de la clase day que chequea si fue la primera vez
    firstTime = week[dayNum].firstTimeCheck(act)

    if (hasTime & firstTime):
        #Agrego al dia la actividad, multiplicada por el numero de horas
#        week[dayNum][act.shift].append(act)*act.hour
        for i in range(act.hours):
            setattr(week[dayNum],act.shift[week[dayNum].dayStartsAt(act.shift)], act)
        if act.days > 1:
            act.days-=1
            chargeDay(week,act)
    else:
        chargeDay(week,act)

    return week,act


def chargeWeek(actVec):
    #creo la semana
    week=[Day()]*5
    #itero en la cantida de actividaddes para cargarlas en dias
    for i in range(len(actVec)):
        week,actVec[i]=chargeDay(week,actVec[i])
    return week



from ActivitiesOrganizer.Prototypes.prototypes import *
import random




def chargeMorning(day,act):
    startsAt = day.actStartsAt(act.shift)
    for i in range(act.hours):
        day.morning[startsAt]=act
        startsAt+=1
    return day
def chargeAfternoon(day,act):
    startsAt = day.actStartsAt(act.shift)
    for i in range(act.hours):
        day.afterNoon[startsAt]=act
        startsAt+=1
    return day


def chargeDay(week,act):
    #si tiene tiempo para la actividad lo carga si no se ejecuta recursivamente

    #Elijo un dia random de la semana
    dayNum= random.randint(0,4)
    print(dayNum)

    print(week[dayNum].morning)
    #Funcion que devuelve index del array que no hay actividades
    timeLeft=week[dayNum].hoursLeft(act.shift)
    print(timeLeft)

    #Devuelve True o False si tiene tiempo para la actividad
    hasTime = timeLeft>=act.hours
    print(hasTime)

    #Funcion de la clase day que chequea si fue la primera vez
    firstTime = week[dayNum].firstTimeCheck(act)
    print(firstTime)

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
        print('')
#        chargeDay(week,act)

    return week,act


def chargeWeek(actVec):
    #creo la semana
    week=[Day()]*5
    print(week)
    #itero en la cantida de actividaddes para cargarlas en dias
    for i in range(len(actVec)):
        week,actVec[i]=chargeDay(week,actVec[i])
    return week



from ActivitiesOrganizer.Prototypes.prototypes import *
import random






def chargeDay(week,act):
    #si tiene tiempo para la actividad lo carga si no se ejecuta recursivamente

    #Elijo un dia random de la semana
    day=week[random.randint(1,5)]

    #Devuelve True o False si tiene tiempo para la actividad
    hasTime = day.hoursLeft(act.shiftCheck())>=act.hours
    #Funcion de la clase day que chequea si fue la primera vez
    firstTime = day.firstTimeCheck(act)

    if (hasTime && firstTime):
        #Agrego al dia la actividad, multiplicada por el numero de horas
        day[act.shiftCheck()].append(act)*act.hours
    else:
        chargeDay(week,act)



def chargeWeek(actVec):
    #creo la semana
    week=[Day()]*5
    #itero en la cantida de actividaddes para cargarlas en dias
    for i in range(len(actVec)):

        chargeDay(week,actVec[i])



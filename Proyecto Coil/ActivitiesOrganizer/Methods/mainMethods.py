from ActivitiesOrganizer.Prototypes.prototypes import *
import random






def chargeDay(week,act):

    #si tiene tiempo para la actividad lo carga si no se ejecuta recursivamente
    day=week[random.randint(1,5)]
    if(day.hoursLeft(act.shiftCheck())>=act.hours ):

        day
        print('hola')
    else:
        chargeDay(week,act)



def chargeWeek(actVec):
    #creo la semana
    week=[Day()]*5
    #itero en la cantida de actividaddes para cargarlas en dias
    for i in range(len(actVec)):

        chargeDay(week,actVec[i])



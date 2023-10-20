from Prototypes.prototypes import Activity


def shiftCheck(shift):
    if shift == 'm':
        return 'morning'
    else:
        return 'afterNoon'

def mainCharge():
    n = int(input('Ingrese cantidad de actividades a cargar: '))
    #Inicializo el array de actividades
    actVec=[None]*n
    #Itero n veces cargando el array con actividades(clase)
    for i in range(n):
        name=input('Ingrese el nombre de la actividad numero '+ str(i) +': ')
        hours=int(input('Ingrese la cantidad de horas: '))
        days=int(input('Ingrese la cantidad de dias: '))
        shift=shiftCheck(input('Manana(m) o tarde(t): '))
        actVec[i]=Activity(name,hours,days,shift)
    #devuelvo un array cargado de actividades
    return actVec



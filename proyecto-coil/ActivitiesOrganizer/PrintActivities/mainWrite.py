

#Aca hay que hacer una funcion que muestre un dia
def writeDay(day):
    #hacer iteracion de todas las horas del dia y mostrar que hay
    for i in range(4):
        print(day.morning[i])
    for i in range(6):
        print(day.afterNoon[i])
    print('\n')

def writeWeek(week):
    #iterar en la semana y mostrar dias
    for i in range(7):
        writeDay(week[i])
    print('')
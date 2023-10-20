


def printMorning(day,i):
    if(i<4):
        return "{:<11}".format(str(day.morning[i]))+' '+str(printMorning(day,i+1))
    return ''
def printAfternoon(day,i):
    if(i<6):
        return "{:<11}".format(str(day.afterNoon[i]))+' '+str(printAfternoon(day,i+1))
    return ''

def printHours(hour):
    if (hour<=17):
        return "{:<11}".format(str(hour)) +' ' + printHours(hour+1)
    return ''

#Aca hay que hacer una funcion que muestre un dia
def writeDay(day):
    #hacer iteracion de todas las horas del dia y mostrar que hay
    for i in range(4):
        print(800+i*100,day.morning[i])
    for i in range(5):
        print(1200+i*100,day.afterNoon[i])
    print('\n')


def writeWeek(week):
    print("{:<11}".format('Hours: ')+printHours(8))
    #iterar en la semana y mostrar dias
    for i in range(5):
        print('Day ',i+1,' ',printMorning(week[i],0)+printAfternoon(week[i],0))

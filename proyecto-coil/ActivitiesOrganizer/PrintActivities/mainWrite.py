


def printMorning(day,i):
    if(i<4):
        return str(day.morning[i])+' '+str(printMorning(day,i+1))
    return ''
def printAfternoon(day,i):
    if(i<6):
        return str(day.afterNoon[i])+' '+str(printMorning(day,i+1))
    return ''

def printHours(hour):
    if (hour<=1800):
        return str(hour) +' ' + printHours(hour+100)
    return ''

#Aca hay que hacer una funcion que muestre un dia
def writeDay(day):
    #hacer iteracion de todas las horas del dia y mostrar que hay
    print(printHours(800))
    for i in range(4):
        print(800+i*100,day.morning[i])
    for i in range(6):
        print(1200+i*100,day.afterNoon[i])
    print('\n')


def writeWeek(week):
    #iterar en la semana y mostrar dias
        for i in range(5):
            print('Day ',i,' ',printMorning(week[i],0)+printAfternoon(week[i],0))
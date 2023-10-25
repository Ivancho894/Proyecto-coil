
def printHours(hour):
    if (hour<=17):
        return "{:<8}".format(str(hour)) +' ' + printHours(hour+1)
    return ''



def writeDay(day,i):
    if(i<10):
        return "{:<8}".format(str(day.activities[i]))+' '+str(writeDay(day,i+1))
    return ''
def writeWeek(week):
    print("{:<8}".format('Hours: ')+printHours(8))
    #iterar en la semana y mostrar dias
    for i in range(5):
        print('Day ',i+1,' ',writeDay(week[i],0))

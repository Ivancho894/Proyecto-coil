
def printHours(hour):
    if (hour<=17):
        return "{:<8}".format(str(hour)) +' ' + printHours(hour+1)
    return ''



def writeDayActivities(day,i):
    if(i<10):
        return "{:<8}".format(str(day.activities[i]))+' '+str(writeDayActivities(day,i+1))
    return ''
def writeDay(day,num):
    days=['Monday','Tuesday','Wensday','Thursday','Friday']
    print("{:<13}".format(days[num]),' ',writeDayActivities(day,0))


def writeWeek(week):
    print("{:<8}".format('Hours: ')+printHours(8))
    #iterar en la semana y mostrar dias
    for i in range(5):
        writeDay(week[i],i)

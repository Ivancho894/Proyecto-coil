class Activity:
    #Metodo constructor de una clase
    def __init__(self,name,hours,days,shift):
        self.name = name
        self.hours = hours
        self.days = days
        self.shift = shift





class Day:
    def __init__(self):
        self.morning  = ['Nothing']*4
        self.afterNoon = ['Nothing']*6
    def freeTime(self,shift,left):
        if(shift == 'morning'):
            if(left):
                return 4-self.nothingCount(shift)
            else:
                return self.nothingCount(shift)
        if (left):
            return 6 - self.nothingCount(shift)
        else:
            return self.nothingCount(shift)

    def nothingCount(self,shift):
        count = 0
        shiftArr = getattr(self,shift)
        for i in range(len(shiftArr)):
            if (shiftArr[i] == 'Nothing'):
                count+=1
        return count


    def hoursLeft(self,shift):
        #verifico que shift la cantidad de nothings y devuelvo el numero de horas libres
        count = 0
        if (shift == 'morning'):
            for i in range(len(self.morning)):
                if (self.morning[i] == 'Nothing'):
                    count += 1
        else:
            for i in range(len(self.afterNoon)):
                if (self.afterNoon[i] == 'Nothing'):
                    count += 1
        return count


    def firstTimeCheck(self,act):
        #verifico si la actividad ya esta en este dia
        shiftArr = getattr(self,act.shift)
        for i in range(len(shiftArr)):
            if (shiftArr[i]==act.name):
                return False
        return True




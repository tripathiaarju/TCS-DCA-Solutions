class Passenger:
    def __init__ (self,passengerName,passengerAge,distanceTravelled):
        self.passengerName = passengerName
        self.passengerAge = passengerAge
        self.distanceTravelled = distanceTravelled
    def calculateTicketFare(self,passengerList,unitFare):
        totalFare = 0
        for i in passengerList:
            if i.passengerAge>=60 or i.passengerAge<12:
                tax = 0
                f = (i.distanceTravelled*unitFare)+tax
                totalFare+=f
            if 21<=i.passengerAge<=59:
                x = (i.distanceTravelled*unitFare)
                tax = (x*12)/100
                f = x+tax
                totalFare+=f
            if 12 <= i.passengerAge <= 20:
                x = (i.distanceTravelled * unitFare)
                tax = (x * 10) / 100
                f = x + tax
                totalFare += f

        return totalFare
    def countSeniorJuniorPaseengers(self,passengerList):
        count = 0
        for i in passengerList:
            if i.passengerAge>=60 or i.passengerAge<12:
                count+=1
        return count
pass_count = int(input())
lis= []
for i in range(pass_count):
    name = input()
    age = int(input())
    dist = int(input())
    obj = Passenger(name,age,dist)
    lis.append(obj)
fare = int(input())
res = obj.calculateTicketFare(lis,fare)
print(res)
count = obj.countSeniorJuniorPaseengers(lis)
print(count)


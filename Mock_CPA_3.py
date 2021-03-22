class Traveller:
    def __init__ (self,travelerName,travelerCountry,travelerAge,countryFrom):
        self.travelerName = travelerName
        self.travelerCountry = travelerCountry
        self.travelerAge = travelerAge
        self.countryFrom = countryFrom
class TravelAgency:
    def __init__ (self,object):
        self.object = object
    def countTravelerTraveledCountry(self,countryName):
        count=0
        for i in self.object:
            for j in i.travelerCountry:
                if countryName == j:
                    count+=1
        return count
    def getTravelerTravelledMaxCountry(self):
        cnt = 0
        name = ""
        for i in self.object:
            if len(i.travelerCountry)>cnt:
                cnt = len(i.travelerCountry)
                name=i.travelerName
        return name


num = int(input())
lis = []
for i in range(num):
    name = input()
    count_country = int(input())
    count_lis = []
    for i in range(count_country):
        travelled_country = input()
        count_lis.append(travelled_country)
    age = int(input())
    f = input()
    obj_Traveller = Traveller(name,count_lis,age,f)
    lis.append(obj_Traveller)
obj_agency = TravelAgency(lis)
name = input()
res1 = obj_agency.countTravelerTraveledCountry(name)
res2 = obj_agency.getTravelerTravelledMaxCountry()
print(res1)
print(res2)
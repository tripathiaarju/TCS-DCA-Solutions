class Item:

    def __init__ (self,itemName,itemType,unitPrice):
        self.itemName = itemName
        self.itemType = itemType
        self.unitPrice = unitPrice

class store:
    
    def __init__(self, itemInventory):
        self.itemInventory= itemInventory

    def buyItem(self,name,quantity):

        for n,q in self.itemInventory.items():

            if name == n.itemName and q >= quantity:
                q = q-quantity
                cost = n.unitPrice * quantity
                print("Bill of the item {} = {}".format(name.lower(),cost))
                self.itemInventory[n] = q

            elif name == n.itemName and q <= quantity and q!=0:
                cost = n.unitPrice * q
                q = q - q
                print("Bill of the item {} = {}".format(name.lower(),cost))
                self.itemInventory[n] = q
num = int(input())
d = {}
lis = []
for i in range(num):
    name = input().capitalize()
    typ = input()
    price= int(input())
    stock = int(input())
    obj_Item = Item(name,typ,price)
    l = dict({obj_Item:stock})
    d.update(l)
    lis.append(name)
obj_store = store(d)
count_to = int(input())
odr_dic = {}
for i in range(count_to):
    name = input().capitalize()
    qty = int(input())
    l = dict({name:qty})
    odr_dic.update(l)

for n,q in odr_dic.items():
    if n in lis:
        obj_store.buyItem(n,q)
    else:
        print(n.lower(),"is not available")

print("Stock in Hand:")
for key,value in obj_store.itemInventory.items():
    print(key.itemName.title(),value)
from enum import Enum


class Ingredient(Enum):
    Mango = "Mango"
    Orange = "Orange"
    Guajana = "Guajana"
    Apple = "Apple"
    Ginger = "Ginger"
    Lemon = "Lemon"
    Guava = "Guava"
    Pineapple = "Pineapple"
    Banana = "Banana"
    Carrot = "Carrot"
    Celery_Stick = "Celery stick"
    Beetroot = "Beetroot"


class Size(Enum):
    Small = 0
    Medium = 1
    Large = 2

    def returnSize(self,s):
        if(s == "Small"):
            return Size.Small
        if(s == "Medium"):
            return Size.Medium
        if(s == "Large"):
            return Size.Large

class Juice:
    _name = ""
    _price = 0
    _sizeFactor = 0
    _listeIngredient = []
    _listeQuantite = []

    def __init__(self, name, price, size, listeIngredient, listeQuantite, debug=False):
        self._name = name
        self._price = price + (0.5 * size.value)
        self._listeIngredient = listeIngredient
        self._listeQuantite = listeQuantite
        if debug:
            print(self._name)
            print(self._listeIngredient)
            print(self._listeQuantite)
            print(self._price)

    def printAll(self):
        print(self._name)
        print(self._listeIngredient)
        print(self._listeQuantite)
        print(self._price)

    @property
    def getName(self):
        return self._name
    @property
    def getPrice(self):
        return self._price
    @property
    def getListeIngredient(self):
        return self._listeIngredient
    @property
    def getListeQuantite(self):
        return self._listeQuantite

class Order :
    _totalPrice = 0
    _juiceList = []

    def __init__(self,debug=False):
        self._juiceList = []
        self._totalPrice = 0
        if debug :
            print(self._juiceList)
            print(self._totalPrice)

    def addJuiceToOrder(self,j,debug=False):
        size = Size.returnSize(None,input("taille : "))
        if debug :
            print(size)
        self._juiceList.append( Juice(j.getName,j.getPrice,size,j.getListeIngredient,j.getListeQuantite,debug) )
        self._totalPrice += self._juiceList.pop().getPrice
        print("Le jus : " + j.getName + " de taille : " + str(size) + " à était ajouté a la commande")

    def showJuiceInOrder(self):
        for i in self._juiceList:
            print("\"" + i.getName + "\"-" + str(i.getPrice) + "$|")
    @property
    def getTotalPrice(self):
        return self._totalPrice

class Barmen() :
    _Order = None
    _jusDispo = None
    def __init__(self):
        self._Order = None
        self._jusDispo = [
            Juice("The Boost", 5, Size.Small, [Ingredient.Mango, Ingredient.Orange, Ingredient.Guajana], [0.5, 2, 1]),
            Juice("The Fresh", 4, Size.Small, [Ingredient.Apple, Ingredient.Ginger, Ingredient.Lemon], [3, 1, 1]),
            Juice("The Fusion", 5, Size.Small, [Ingredient.Guava, Ingredient.Pineapple, Ingredient.Banana], [1, 0.25, 0.5]),
            Juice("The Detox", 3.5, Size.Small, [Ingredient.Carrot, Ingredient.Celery_Stick, Ingredient.Beetroot], [3, 1, 1])
        ]
    def createOrder(self,debug=False):
        self._Order = Order(debug)
    def addToOrder(self,debug=False):
        userChoice = input("Jus : ")
        while( userChoice != "annuler" and userChoice != "fin") :
            for i in self._jusDispo:
                if userChoice == i.getName:
                    jusToAdd = i
                    if debug :
                        print("jus existe")
                    break
            self._Order.addJuiceToOrder(jusToAdd,debug)
            self._Order.showJuiceInOrder()
            userChoice = input("Jus : ")
        if userChoice == "annuler" :
            self._Order = None
            print("commande annuler")
        if userChoice == "fin":
            print("commande finaliser")
            print("Le montant est de : " + str(self._Order.getTotalPrice ) + "$" )

    def showOrder(self):
        print(self._Order)

    def getListeJusDispo(self,index=None):
        if index == None:
            return self._jusDispo
        else :
            return self._jusDispo[index].printAll()

if __name__ == '__main__':
    DEBUG = True
    b = Barmen()
    b.createOrder()
    b.addToOrder()

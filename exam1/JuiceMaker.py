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

class Order :
    _totalPrice = 0
    _juiceList = []

    def __init__(self,JuiceList):
        self._juiceList = JuiceList

class Barmen :
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

    def addNewOrder(self):
        print("Menu :")
        for i in self._jusDispo:
            print("Nom : " + str(i.getName))
            print("Price pour petit : " + str(i.getPrice))

    def getListeJusDispo(self,index=None):
        if index == None:
            return self._jusDispo
        else :
            return self._jusDispo[index].printAll()

if __name__ == '__main__':
    DEBUG = True
    b = Barmen()
    b.addNewOrder()
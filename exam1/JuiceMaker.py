from enum import Enum
# A travès le programme, on peut trouver des bools nommé "debug"
# Ils sont uniquement utiliser pour print certain element lors du developpement
# Enum des ingredient
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

# Enum utiliser pour la taille du jus
class Size(Enum):
    Small = 0
    Medium = 1
    Large = 2
    # Permet de retourner l'Enum correspondant a la string entré
    def returnSize(self,s):
        if(s == "Small"):
            return Size.Small
        if(s == "Medium"):
            return Size.Medium
        if(s == "Large"):
            return Size.Large
# Classe JUS !
class Juice:
    _name = ""
    _price = 0
    # L'attribut sizeFactor sert au calcul du prix du jus en fonction de sa taille
    _sizeFactor = 0
    # Les deux listes suivante serviront a une futur update
    # permetant de gérer les stocks d'ingrédient
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

    # On initialise un order (commande) avec une liste de jus commandé vide
    # ainsi que le prix total de l'ordre en cour
    # (évolution possible : gestion de plusieurs commande simultané)
    def __init__(self,debug=False):
        self._juiceList = []
        self._totalPrice = 0
        if debug :
            print(self._juiceList)
            print(self._totalPrice)
    # Utiliser pour ajouter un jus (séléctionner par l'utilisateur) à la commande (Order)
    def addJuiceToOrder(self,j,debug=False):
        # Input de la taille par le client
        size = Size.returnSize(None,input("taille : "))
        if debug :
            print(size)
        # Ajout du jus a la liste de jus de la commande
        self._juiceList.append( Juice(j.getName,j.getPrice,size,j.getListeIngredient,j.getListeQuantite,debug) )
        # On ajoute au prix total le prix du jus que l'on vien d'ajouter dans la commande
        self._totalPrice += self._juiceList[-1].getPrice
        print("Le jus : " + j.getName + " de taille : " + str(size) + " à était ajouté a la commande")
    # Affiche tout les jus de la commande
    def showJuiceInOrder(self):
        for i in self._juiceList:
            print("\"" + i.getName + "\"-" + str(i.getPrice) + "$|")

    @property
    def getTotalPrice(self):
        return self._totalPrice

class Barmen() :
    _Order = None
    _jusDispo = None
    # Par defaut, un barman est initialiser avec une liste de jus qu'il "sais faire" et aucune commande
    # Chaque jus est initialiser en dur
    # Une méthode learnNewJuice pourrais être ajouter au barmen afin qu'il puisse réaliser plus de jus differents !
    def __init__(self):
        self._Order = None
        self._jusDispo = [
            Juice("The Boost", 5, Size.Small, [Ingredient.Mango, Ingredient.Orange, Ingredient.Guajana], [0.5, 2, 1]),
            Juice("The Fresh", 4, Size.Small, [Ingredient.Apple, Ingredient.Ginger, Ingredient.Lemon], [3, 1, 1]),
            Juice("The Fusion", 5, Size.Small, [Ingredient.Guava, Ingredient.Pineapple, Ingredient.Banana], [1, 0.25, 0.5]),
            Juice("The Detox", 3.5, Size.Small, [Ingredient.Carrot, Ingredient.Celery_Stick, Ingredient.Beetroot], [3, 1, 1])
        ]
    # Appeler lorqu'un client ouvre une commande
    def createOrder(self,debug=False):
        self._Order = Order(debug)
    # Ajout un(des) nouveau(x) jus a la commande
    def addToOrder(self,debug=False):
        userChoice = input("Veuillez saisir le nom du jus voulu : ")
        # Si l'utilisateur saisi "annuler" alors la commander est annuler et "détruite"
        # Si l'utilisateur saisi "fin" alors la commander est finaliser et en attente de payement
        while( userChoice != "annuler" and userChoice != "fin") :
            # La boucle regarde si le jus entrée par l'utilisateur est bien réalisable par le barmen
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

if __name__ == '__main__':
    DEBUG = True
    # On crée le barmen
    b = Barmen()
    # On crée la commande
    b.createOrder()
    # On ajoute un ou plusieurs jus
    b.addToOrder()
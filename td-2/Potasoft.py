class Zone():

    def __init__(self,long=10,larg=10,obj=None):
        self.long = long
        self.larg = larg
        if type(obj) is Legume :
            self.zoneLegume = ZoneLegume(obj)
        if type(obj) is Fruit :
            self.zoneFruit = ZoneFruit(obj)

class ZoneLegume():
    def __init__(self,leg):
        self.nom = "Mes Légumes"
        self.legume[0] = leg

class ZoneFruit():
    def __init__(self,frt):
        self.nom = "Mes Fruits"
        self.fruit[0] = frt

class Legume():
    def __init__(self,nom):
        self.nom = nom

class Fruit():
    def __init__(self,nom):
        self.nom = nom

class Primeur():
    nom = ""
    zone = Zone()

    def __init__(self,nom,obj=None):
        self.nom = nom
        if obj == None :
            self.zone[0] = Zone()
        else :
            self.zone[0] = Zone(obj)

        print( "Primeur : " + self.nom )

P = Primeur("Gerard",Fruit("Banane"))

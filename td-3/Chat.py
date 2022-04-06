from enum import Enum


class Classification(Enum):
    POISSON = 0
    INSECTE = 1
    OISEAU = 2
    MAMIFERE = 3
    AMPHIBIEN = 4
    REPTILE = 5
    IVERTEBRER = 6


class Animal:
    _nom = ""
    _classification = None
    _isCute = False

    def __init__(self, nom, classification, cutness=False):
        self._nom = nom
        self._classification = classification
        self._isCute = cutness
        print("L'animal : " + self._nom + " à été crée |type : " + str(self._classification))

    @property
    def classification(self):
        return self._classification

    @property
    def isCute(self):
        return self._isCute

    @property
    def nom(self):
        return self._nom


class Chat(Animal):
    def __init__(self, nom, classification):
        super().__init__(nom, classification, True)
        print("Le chat : " + self._nom + " à été crée |type : " + str(self._classification))


class Chien(Animal):
    def __init__(self, nom, classification):
        super().__init__(nom, classification)
        print("Le chien : " + self._nom + " à été crée |type : " + str(self._classification))


animal = Animal("Osama", Classification.MAMIFERE)
chat = Chat("Minou", Classification.MAMIFERE)
chien = Chien("Rheun", Classification.MAMIFERE)

if chat.isCute:
    print(chat.nom + " est mignon")
else:
    print(chat.nom + " est pas mignon")

if chien.isCute:
    print(chien.nom + " est mignon")
else:
    print(chien.nom + " est pas mignon")
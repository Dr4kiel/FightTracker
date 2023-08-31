'''
Fichier contenant les classes des personnages et des monstres
'''

from EntityView import EntityView


class Entite():

    def __init__(self, name, initiative, hp, ac, speed, controller, **kwargs):
        '''
        Constructeur de la classe
        '''
        self.name = name
        self.initiative = initiative
        self.hp = hp
        self.ac = ac
        self.speed = speed
        self.controller = controller

    def show(self):
        '''
        Méthode permettant d'afficher l'entité
        '''
        self.controller.show(self)

    def __str__(self):
        '''
        Méthode permettant d'afficher l'entité
        '''
        return self.name + " : " + str(self.initiative) + " Initiative"

    def __repr__(self):
        '''
        Méthode permettant d'afficher l'entité
        '''
        return self.name + " : " + str(self.initiative) + " Initiative"

    def __lt__(self, other):
        '''
        Méthode permettant de comparer deux entités
        '''
        return self.initiative < other.initiative

    def __gt__(self, other):
        '''
        Méthode permettant de comparer deux entités
        '''
        return self.initiative > other.initiative

    def __eq__(self, other):
        '''
        Méthode permettant de comparer deux entités
        '''
        return self.initiative == other.initiative

    def __le__(self, other):
        '''
        Méthode permettant de comparer deux entités
        '''
        return self.initiative <= other.initiative

    def __ge__(self, other):
        '''
        Méthode permettant de comparer deux entités
        '''
        return self.initiative >= other.initiative

    def __ne__(self, other):
        '''
        Méthode permettant de comparer deux entités
        '''
        return self.initiative != other.initiative

    def set_view(self, view):
        '''
        Méthode permettant de définir la vue de l'entité
        '''
        self.view = view

    def get_view(self):
        '''
        Méthode permettant de récupérer la vue de l'entité
        '''
        return self.view


class Personnage(Entite):

    def __init__(self, name, initiative, hp, ac, speed, controller, **kwargs):
        super().__init__(name, initiative, hp, ac, speed, controller, **kwargs)


class Monstre(Entite):

    def __init__(self, name, initiative, hp, ac, speed, controller, **kwargs):
        super().__init__(name, initiative, hp, ac, speed, controller, **kwargs)

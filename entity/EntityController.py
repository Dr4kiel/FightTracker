'''
Fichier contenant le contrôleur des entités
'''


class EntityController:

    def __init__(self, controller, **kwargs):
        '''
        Constructeur de la classe
        '''
        self.controller = controller
        self.entities = []

    def add_entity(self, entity):
        '''
        Méthode permettant d'ajouter une entité
        '''
        self.entities.append(entity)

    def remove_entity(self, entity):
        '''
        Méthode permettant de supprimer une entité
        '''
        self.entities.remove(entity)

    def show(self, entity):
        '''
        Méthode permettant d'afficher une entité
        '''
        self.controller.show(entity)

    def show_all(self):
        '''
        Méthode permettant d'afficher toutes les entités
        '''
        for entity in self.entities:
            print(entity)

    def sort(self):
        '''
        Méthode permettant de trier les entités
        '''
        self.entities.sort(key=lambda x: x.initiative, reverse=True)

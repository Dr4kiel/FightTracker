'''
Fichier contenant les classes des pages de l'application
'''

# Imports
from tkinter import *
import customtkinter as ctk
from PIL import Image

from entity.EntityController import EntityController
from entity.Entity import Entite
from component.EntityView import EntityView
from component.fancyElement import FancySpinBox

DEFAULT_BACKGROUND = '#41B77F'
WHITE_BACKGROUND = '#FFFFFF'


class Page(ctk.CTkFrame):
    '''
    Classe représentant une page de l'application
    '''

    def __init__(self, window, controller, **kwargs):
        '''
        Constructeur de la classe
        '''
        ctk.CTkFrame.__init__(self, window, **kwargs)
        self.window = window
        self.controller = controller

    def show(self):
        '''
        Méthode permettant d'afficher la page
        '''
        self.pack(expand=YES, fill=BOTH)

    def hide(self):
        '''
        Méthode permettant de cacher la page
        '''
        self.pack_forget()


class PageDemarrage(Page):
    '''
    Classe représentant la page de démarrage de l'application
    '''

    def __init__(self, window, controller, **kwargs):
        '''
        Constructeur de la classe
        '''
        Page.__init__(self, window, controller, **kwargs)

        # Création de la frame principale
        frame = ctk.CTkFrame(self)

        # Création du titre
        label_title = ctk.CTkLabel(frame, text="D&D Combat Tracker", font=(
            "Courrier", 40))
        label_title.pack(expand=YES)

        # Création du bouton de lancement
        launch_button = ctk.CTkButton(frame, text="Commencer", font=(
            "Courrier", 25), command=self.launch)

        launch_button.pack(expand=YES)

        # Afficjage de la frame
        frame.pack(expand=YES, fill=BOTH)

    def launch(self):
        '''
        Méthode permettant de lancer l'application
        '''
        self.hide()
        self.controller.show_page("config")


class PageConfiguration(Page):
    '''
    Classe représentant la page de configuration de l'application
    '''

    def __init__(self, window, controller, **kwargs):
        '''
        Constructeur de la classe
        '''
        Page.__init__(self, window, controller, **kwargs)

        self.entity_controller = EntityController(self.controller)

        # Création de la frame principale
        frame = ctk.CTkFrame(self)

        # Création du titre
        label_title = ctk.CTkLabel(frame, text="Configuration", font=(
            "Courrier", 40))
        label_title.pack(expand=YES)

        # Création du frame de la liste des entités
        entity_list_frame = ctk.CTkFrame(frame)
        entity_list_frame.pack(expand=YES)

        # Création de la liste des entités avec un text edit en bloquant la modification
        self.entity_list = ctk.CTkFrame(entity_list_frame)
        self.entity_list.pack(expand=YES, side=BOTTOM, padx=10, pady=10)

        # Création du frame des boutons de la liste des entités
        entity_list_button_frame = ctk.CTkFrame(
            entity_list_frame)
        entity_list_button_frame.pack(
            expand=YES, side=RIGHT, padx=10, pady=10, fill=X)

        # Création du bouton d'ajout d'entité
        add_entity_button = ctk.CTkButton(entity_list_button_frame, text="", image=ctk.CTkImage(light_image=Image.open("./assets/add_ico.png")), font=(
            "Courrier", 25), command=self.add_entity_window, fg_color="green", width=20)
        add_entity_button.pack(expand=YES, side=RIGHT,
                               padx=10, pady=10)

        # Création du groupe de boutons de navigation
        navigation_frame = ctk.CTkFrame(frame)
        navigation_frame.pack(expand=YES)

        # Création du bouton de lancement
        launch_button = ctk.CTkButton(navigation_frame, text="Lancer", font=(
            "Courrier", 25), command=self.launch)
        launch_button.pack(expand=YES, side=LEFT, padx=10, pady=10)

        # Création du bouton de retour
        return_button = ctk.CTkButton(navigation_frame, text="Retour", font=(
            "Courrier", 25), command=self.return_home)

        return_button.pack(expand=YES, side=RIGHT, padx=10, pady=10)

        # Afficjage de la frame
        frame.pack(expand=YES, fill=BOTH)

    def return_home(self):
        '''
        Méthode permettant de retourner à la page d'accueil
        '''
        self.hide()
        self.controller.show_page("home")

    def launch(self):
        '''
        Méthode permettant de lancer l'application
        '''
        self.hide()

        self.controller.set_entity_controller(self.entity_controller)

        self.controller.show_page("combat")

    def add_entity_window(self):
        '''
        Méthode permettant d'ajouter une entité
        '''

        # Création de la fenêtre
        window = Toplevel(self.window)
        window.title("Ajouter une entité")
        window.geometry("720x480")
        window.minsize(480, 360)
        window.iconbitmap("assets/icon.ico")

        # Création du frame principal
        frame = ctk.CTkFrame(window)
        frame.pack(expand=YES)

        # Création du frame de l'entité
        entity_frame = ctk.CTkFrame(frame)
        entity_frame.pack(expand=YES)

        # Création du frame du nom de l'entité
        entity_name_frame = ctk.CTkFrame(entity_frame)
        entity_name_frame.pack(expand=YES, fill=X)

        # Création du label du nom de l'entité
        entity_name_label = ctk.CTkLabel(entity_name_frame, text="Nom", font=(
            "Courrier", 25))
        entity_name_label.pack(expand=YES, side=LEFT, padx=10, pady=10)

        # Création de l'entrée du nom de l'entité
        entity_name_entry = ctk.CTkEntry(entity_name_frame, font=(
            "Courrier", 25))
        entity_name_entry.pack(expand=YES, side=RIGHT, fill=X)
        entity_name_entry.delete(0, END)
        entity_name_entry.insert(0, "Derg")

        # Création du frame de l'initiative de l'entité
        entity_initiative_frame = ctk.CTkFrame(
            entity_frame)
        entity_initiative_frame.pack(expand=YES, fill=X)

        # Création du label de l'initiative de l'entité
        entity_initiative_label = ctk.CTkLabel(entity_initiative_frame, text="Initiative", font=(
            "Courrier", 25))
        entity_initiative_label.pack(
            expand=YES, side=LEFT, padx=10, pady=10)

        # Création de l'entrée de l'initiative de l'entité
        entity_initiative_entry = FancySpinBox(
            entity_initiative_frame, value=10, width=20)
        entity_initiative_entry.pack(side=RIGHT, fill=X)

        # Création du frame des points de vie de l'entité
        entity_hp_frame = ctk.CTkFrame(entity_frame)
        entity_hp_frame.pack(expand=YES, fill=X)

        # Création du label des points de vie de l'entité
        entity_hp_label = ctk.CTkLabel(entity_hp_frame, text="Points de vie", font=(
            "Courrier", 25))
        entity_hp_label.pack(expand=YES, side=LEFT, padx=10, pady=10, fill=X)

        # Création de l'entrée des points de vie de l'entité
        entity_hp_entry = FancySpinBox(
            entity_hp_frame, value=20, width=20)
        entity_hp_entry.pack(side=RIGHT)

        # Création du frame de la classe d'armure de l'entité
        entity_ac_frame = ctk.CTkFrame(entity_frame)
        entity_ac_frame.pack(expand=YES, fill=X)

        # Création du label de la classe d'armure de l'entité
        entity_ac_label = ctk.CTkLabel(entity_ac_frame, text="Classe d'armure", font=(
            "Courrier", 25))
        entity_ac_label.pack(expand=YES, side=LEFT, padx=10, pady=10, fill=X)

        # Création de l'entrée de la classe d'armure de l'entité
        entity_ac_entry = FancySpinBox(
            entity_ac_frame, value=10, width=20)
        entity_ac_entry.pack(side=RIGHT)

        # Création du frame de la vitesse de l'entité
        entity_speed_frame = ctk.CTkFrame(entity_frame)
        entity_speed_frame.pack(expand=YES, fill=X)

        # Création du label de la vitesse de l'entité
        entity_speed_label = ctk.CTkLabel(entity_speed_frame, text="Vitesse", font=(
            "Courrier", 25))
        entity_speed_label.pack(expand=YES, side=LEFT,
                                padx=10, pady=10, fill=X)

        # Création de l'entrée de la vitesse de l'entité
        entity_speed_entry = FancySpinBox(
            entity_speed_frame, value=12, width=20)
        entity_speed_entry.pack(side=RIGHT)

        # Création du frame des boutons
        button_frame = ctk.CTkFrame(frame)
        button_frame.pack(expand=YES, fill=X)

        # Création du bouton de validation
        validate_button = ctk.CTkButton(button_frame, text="Valider", font=(
            "Courrier", 25), command=lambda: self.append_an_entity(entity_name_entry.get(), entity_initiative_entry.get(), entity_hp_entry.get(), entity_ac_entry.get(), entity_speed_entry.get()) and window.destroy())
        validate_button.pack(expand=YES, side=LEFT, padx=10, pady=10)

        # Création du bouton d'annulation
        cancel_button = ctk.CTkButton(button_frame, text="Annuler", font=(
            "Courrier", 25), command=window.destroy)
        cancel_button.pack(expand=YES, side=RIGHT, padx=10, pady=10)

    def append_an_entity(self, entity_name, entity_initiative, entity_hp, entity_ac, entity_speed):
        '''
        Méthode permettant d'ajouter une entité
        '''
        entity = Entite(entity_name, entity_initiative, entity_hp,
                        entity_ac, entity_speed, self.entity_controller)

        self.entity_controller.add_entity(entity)

        # on récupère le dernier groupe d'entité créé
        last_group = self.entity_list.winfo_children()[len(
            self.entity_list.winfo_children()) - 1] if len(self.entity_list.winfo_children()) > 0 else None

        # création d'un groupe d'entité si aucun n'existe et création d'un groupe toutes les 6 entités
        if len(self.entity_controller.entities) % 6 == 1 or last_group == None:
            last_group = ctk.CTkFrame(self.entity_list)
            last_group.pack(expand=YES, side=LEFT, padx=10, pady=10)

        frame_elem = ctk.CTkFrame(last_group)
        frame_elem.pack(expand=YES, side=TOP, padx=10, pady=10)

        elem = ctk.CTkLabel(frame_elem, text=entity.__str__())
        elem.pack(expand=YES, side=LEFT, padx=10, pady=10)

        # Création du bouton de suppression d'entité
        remove_entity_button = ctk.CTkButton(frame_elem, text="", image=ctk.CTkImage(light_image=Image.open("./assets/delete_ico.png")), font=(
            "Courrier", 25), command=lambda: self.remove_entity(frame_elem, entity), fg_color="red", width=20)
        remove_entity_button.pack(expand=YES, side=RIGHT, padx=10, pady=10)

        return True

    def remove_entity(self, frame, entity):
        '''
        Méthode permettant de supprimer une entité
        '''
        self.entity_controller.remove_entity(entity)
        frame.destroy()

        # on vérifie si il y a un groupe d'entité vide
        for group in self.entity_list.winfo_children():
            if len(group.winfo_children()) == 0:
                group.destroy()


class PageCombat(Page):
    '''
    Classe représentant la page de configuration de l'application
    '''

    def __init__(self, window, controller, **kwargs):
        '''
        Constructeur de la classe
        '''
        Page.__init__(self, window, controller, **kwargs)

        # Création de la frame principale
        frame = ctk.CTkFrame(self)

        # Création de la frame des entités
        self.entity_frame = ctk.CTkFrame(frame)
        self.entity_frame.pack(expand=YES)

        # Création du frame des boutons
        button_frame = ctk.CTkFrame(frame)
        button_frame.pack(expand=YES)

        # Création du bouton de retour
        return_button = ctk.CTkButton(button_frame, text="Retour", font=(
            "Courrier", 25), command=self.return_config)
        return_button.pack(expand=YES, side=RIGHT, padx=10, pady=10)

        # Afficjage de la frame
        frame.pack(expand=YES, fill=BOTH)

    def return_config(self):
        '''
        Méthode permettant de retourner à la page de configuration
        '''
        self.hide()
        self.controller.show_page("config")

    def update_entity_controller(self, entity_controller):
        '''
        Méthode permettant de mettre à jour le contrôleur des entités
        '''
        self.entity_controller = entity_controller

        # Suppression des entités précédentes
        for entity in self.entity_frame.winfo_children():
            entity.destroy()

        # Tri des entités
        self.entity_controller.sort()

        # Création des entités
        for entity in self.entity_controller.entities:
            entity_view = EntityView(
                self.entity_frame, self.controller)
            entity_view.pack(expand=YES, side=LEFT, padx=10, pady=10)
            entity_view.show(entity)

        # Affichage des entités
        self.entity_frame.pack(expand=YES)


class Controller:
    '''
    Classe représentant le contrôleur de l'application
    '''

    def __init__(self):
        '''
        Constructeur de la classe
        '''
        # Création de la fenêtre
        self.window = ctk.CTk()
        self.window.title("D&D Combat Tracker")
        self.window.geometry("1280x720")
        self.window.minsize(480, 360)
        self.window.iconbitmap("assets/icon.ico")
        self.entity_controller = EntityController(self)

        # Création d'une énumération des pages
        self.pages = {
            "home": PageDemarrage(self.window, self),
            "config": PageConfiguration(self.window, self),
            "combat": PageCombat(self.window, self)
        }

        # Affichage de la page d'accueil
        self.show_page("home")

        # Affichage de la fenêtre
        self.window.mainloop()

    def show_page(self, page):
        '''
        Méthode permettant d'afficher une page
        '''
        self.pages[page].show()

    def hide_page(self, page):
        '''
        Méthode permettant de cacher une page
        '''
        self.pages[page].hide()

    def set_entity_controller(self, entity_controller):
        '''
        Méthode permettant de définir le contrôleur des entités
        '''
        self.entity_controller = entity_controller

        self.pages["combat"].update_entity_controller(entity_controller)

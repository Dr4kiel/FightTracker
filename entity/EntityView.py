'''
Fichier contenant les vues des entités
'''

# Imports
from tkinter import *
import customtkinter as ctk
from PIL import Image


class EntityView(ctk.CTkFrame):

    def __init__(self, window, controller, **kwargs):
        '''
        Constructeur de la classe
        '''
        ctk.CTkFrame.__init__(self, window, **kwargs)
        self.window = window
        self.controller = controller

        # Création des labels
        self.label_name = ctk.CTkLabel(self, text="Nom")
        self.label_initiative = ctk.CTkLabel(
            self, text="Initiative", image=ctk.CTkImage(
                light_image=Image.open("./assets/star.png")), compound=LEFT, justify=RIGHT)
        self.label_hp = ctk.CTkLabel(
            self, text="Points de vie", image=ctk.CTkImage(
                light_image=Image.open("./assets/heart.png")), compound=LEFT, justify=RIGHT)
        self.label_ac = ctk.CTkLabel(
            self, text="Classe d'armure", image=ctk.CTkImage(
                light_image=Image.open("./assets/shield.png")), compound=LEFT, justify=RIGHT)
        self.label_speed = ctk.CTkLabel(self, text="Vitesse", image=ctk.CTkImage(
            light_image=Image.open("./assets/speed.png")), compound=LEFT, justify=RIGHT)

    def show(self, entity):
        '''
        Méthode permettant d'afficher l'entité
        '''
        self.label_name.pack(expand=YES, padx=20)
        self.label_initiative.pack(expand=YES, padx=20)
        self.label_hp.pack(expand=YES, padx=20)
        self.label_ac.pack(expand=YES, padx=20)
        self.label_speed.pack(expand=YES, padx=20)

        self.update(entity)

    def hide(self):
        '''
        Méthode permettant de cacher l'entité
        '''
        self.label_name.pack_forget()
        self.label_initiative.pack_forget()
        self.label_hp.pack_forget()
        self.label_ac.pack_forget()
        self.label_speed.pack_forget()

    def update(self, entity):
        '''
        Méthode permettant de mettre à jour l'entité
        '''
        self.label_name.configure(text=entity.name)
        self.label_initiative.configure(text=entity.initiative)
        self.label_hp.configure(text=entity.hp)
        self.label_ac.configure(text=entity.ac)
        self.label_speed.configure(text=entity.speed)

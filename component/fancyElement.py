'''
Fichiers contenant les classes des éléments graphiques personnalisés
'''

# Imports
from tkinter import *
import customtkinter as ctk


class FancySpinBox(ctk.CTkFrame):

    def __init__(self, window, min=0, max=100, value=0, **kwargs):
        super().__init__(window, **kwargs)

        self.min = min
        self.max = max

        # Création des widgets
        self.minus_button = ctk.CTkButton(
            self, text="-", command=self.minus, width=20)

        self.value = ctk.CTkEntry(self, width=100, justify=CENTER)
        self.value.insert(0, str(value))

        # proteger le label pour que l'utilisateur ne puisse entrer que des chiffres et effacer
        self.value.bind(
            "<Key>", lambda e: "break" if e.char not in ('0123456789\x08') else None)

        self.plus_button = ctk.CTkButton(
            self, text="+", command=self.plus, width=20)

        # Placement des widgets
        self.minus_button.pack(side=LEFT, expand=YES)
        self.value.pack(side=LEFT, expand=YES, padx=20)
        self.plus_button.pack(side=LEFT, expand=YES)

    def minus(self):
        '''
        Méthode permettant de décrémenter la valeur
        '''

        if self.value.get() == '':
            self.value.insert(0, 0)

        number = int(self.value.get())
        if number > self.min:
            self.value.delete(0, END)
            self.value.insert(0, number - 1)

    def plus(self):
        '''
        Méthode permettant d'incrémenter la valeur
        '''

        if self.value.get() == '':
            self.value.insert(0, 0)

        number = int(self.value.get())
        if number < self.max:
            self.value.delete(0, END)
            self.value.insert(0, number + 1)

    def get(self):
        '''
        Méthode permettant de récupérer la valeur
        '''
        return int(self.value.get()) if self.value.get() != '' else 0

    def set(self, value):
        '''
        Méthode permettant de définir la valeur
        '''
        self.value.delete(0, END)
        self.value.insert(0, value)

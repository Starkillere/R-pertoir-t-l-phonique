#!/usr/bin/env python3
# -*- coding: utf-8 -*-

####IMPORTATION####
import tkinter as tk
from tkinter import*
import csv
import random
from tkinter.font import BOLD

### CLASS Repertoire ###
class Repertoire:

    '''La class repertoir permet de crée un repetoire téléphonique qui dispose de plusieurs fonctionnalité:
            - Rechercher un contact en fonction de son nom,
            - Supprimer un contact,
            - Afficher tout les contacte du répertoir,
            - Génerer un contatct aléatoir.
            - Modifier un contact.

        Modules:
        --------
        csv
        randome

        Atributs:
        ---------
        self.fichier: type str, valeur pardéfaut (repertoir.csv) type fichier csv

        Méthodes:
        ---------
        __init__: constructeur.
        modifier_fichier_repertoire: permet de modifier l'atribut sefl.fichier.
        __verifier_contact: vérifie si les contacte n'on pas le même numero (méthode privé).
        ajouter_contact: permet d'ajouter un nouveau contact.
        rechercher_contact: permet de rechercher un contact dans le fichier repertoire en avec le nom le numéro ou le nom ou encore le prenom.
        supprimer_contact: permet de suprprimer un contact.
        modifier_contact: permet de modifier un contact.
        afficher_repertoire: permet d'afficher le répertoire.
        randome_contac: permet de crée des contact aléatoire.

    '''

    def __init__(self):
        self.fichier = 'repertoire.csv'

    def modifier_fichier_repertoire(self, fichier:str):
        '''Modifiez votre fichier répertoir. Le repertoir dois être un fichier csv !'''
        self.fichier = fichier
    
    def __verifier_contact(self, numero:str):
        '''Vérifier que le numéro saisie n'est pas déjà associé à un autre contact'''
        with open(self.fichier, 'r', encoding='utf-8') as fichier:
            reader = csv.reader(fichier)
            for concernannt in  reader:
                if concernannt[2] == numero:
                    break
            else:
                return False
        return True
                    
    def ajouter_contact(self, nom:str, prenom:str, numero:str):
        '''Ajouter un nouveau contact, paramétres obligatoir nom prénom, numéro, le numéro de type str'''
        if self.__verifier_contact(numero):
            with open("repertoire.csv",'a', encoding='utf-8') as fichier:
              csv_writer = csv.writer(fichier, delimiter=',')
              csv_writer.writerow([nom.capitalize(), prenom.capitalize(), numero])
            return True    
        else:
            return False

    def rechercher_contact(self, nom:str=None, prenom:str=None, numero:str=None):
        '''Rechercher un contact. Vous pouvez saisir son nom ou son prenom ou encore son numero, des type str valeur par défaut None'''
        def forme(index:int, value:str):
            '''Cette fonction permet d'éviter les répetition'''
            with open("repertoire.csv",'r', encoding='utf-8') as fichier:
                reader = csv.reader(fichier)
                for data in reader:
                    if data != []:
                        if data[index] == value.capitalize():
                         return data
        if nom != None:
            return forme(0, nom)
        elif prenom != None:
            return forme(1, prenom)
        elif numero != None:
            return forme(2, numero)
        else:
            return False
    
    def supprimer_contact(self, nom:str=None, prenom:str=None, numero:str=None):
        '''Spprimer un contact. Vous pouvez saisir son nom ou son prenom ou encore son numero, des type str valeur par défaut None'''
        def forme(index, value):
            '''Cette fonction permet d'éviter les répetition'''
            contacts = []
            with open("repertoire.csv",'r', encoding='utf-8') as fichier:
                reader = csv.reader(fichier)
                for i in reader:
                    if i != []:
                        if i[index] != value:
                            contacts.append(i)
            with open("repertoire.csv",'w', encoding='utf-8') as fichier:
                csv_writer = csv.writer(fichier, delimiter=',')
                for i in contacts:
                    csv_writer.writerow(i)
        if nom != None:
            return forme(0, nom)
        elif prenom != None:
            return forme(1, prenom)
        elif numero != None:
            return forme(2, numero)
        else:
            return False

    def modifier_contact(self, nom:str=None, prenom:str=None, numero:str=None, new_nom:str=None, new_prenom:str=None, new_numero:str=None):
        '''Modifier un contact, permet de modifier un contact:
            - Pour modifier son nom il faut saisir en paramétre: son nom dans la variable nom et son nouveau nom dans la variable new_nom.
            - Pour modifier son prénom il faut saisir en paramétre: son prénom dans la variable prenom et son nouveau prénom dans la variable new_Prénom.
            - Pour modifier son numéro il faut saisir en paramétre: son numéro dans la variable numero et son nouveau nom dans la variable new_numero.
        '''
        contact_a_modifier = self.rechercher_contact(nom, prenom, numero)
        self.supprimer_contact(contact_a_modifier)
        contact_modifier = []
        if new_nom != None:
            contact_modifier.append(new_nom)
        else:
            contact_modifier.append(contact_a_modifier[0])
        if new_prenom != None:
            contact_modifier.append(new_prenom)
        else:
            contact_modifier.append(contact_a_modifier[1])
        if new_numero != None:
            contact_modifier.append(new_numero)
        else:
            contact_modifier.append(contact_a_modifier[2])
        self.ajouter_contact(contact_modifier[0], contact_modifier[1], contact_modifier[2])

    def afficher_repertoire(self):
        '''Cette méthode permet d'affciher tout le répertoire! elle ne prends pas de paramétres'''
        repertoire = []
        with open("repertoire.csv",'r', encoding='utf-8') as fichier:
            reader = csv.reader(fichier)
            for data in reader:
                if data != []:
                    repertoire.append(data)
        return repertoire

    def randome_contact(self):
        '''Cette méthode permet de crée un contact aléatoir. elle ne prend aucun paramétre'''
        lettre = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
	              'o', 'p', 'q', 'r', 's', 't', 'u',
	              'h', 'i', 'j', 'k', 'l', 'm', 'n',
	              'v', 'w', 'x', 'y', 'z',]

        nombre = ['1', '2', '3', '4','5', '6', '7', '8', '9', '0']
        departement = ['0692','0693','0262']

        nom  = ''
        prenom = ''
        numero = ''

        #nom aléatoir
        for i in range(random.choice([3,4,5,6,7])):
            nom += random.choice(lettre).upper()

        #Prénom alèatoir
        for i in range(random.choice([3,4,5,6,7])):
            prenom += random.choice(lettre)
        prenom = prenom.capitalize()

        #numéro aléatoir
        numero += random.choice(departement)
        for i in range(6):
            numero += random.choice(nombre)

        self.ajouter_contact(nom, prenom, numero)
        return [nom, prenom, numero]

###CLASS APP###
class App():

    '''class App crée une fenêtre GUI
    '''
    def __init__(self, root):
        self.ajouter = False
        self.rechercher = False
        self.supprimer = False
        self.afficherall = False
        self.generer = False
        self.modifier = False
        #Fenetre principale
        self.repertoir = Repertoire()
        self.text_var = StringVar()
        self.root = root
        self.root.geometry("1000x700")
        self.root.title("Répertoire")
        self.root.config(background="#73878F")

        self.label = Label(root, text="Bienvenue dans votre répertoire !", bg="#73878F", fg='#000506', font=('Arial', 30, 'bold'))
        self.entry = tk.Entry(root, width=30, border=10, fg='blue', font=('Arial', 12, 'bold'), textvariable=self.text_var)

        self.b1 = Button(root, text ="Rechercher un contact", relief=RAISED, command=self._rechercher)
        self.b2 = Button(root, text ="Supprimer un contact", relief=RAISED,command=self._supprimer)
        self.b3 = Button(root, text ="Modifier un contact", relief=RAISED,command=self._modifier)
        self.b4 = Button(root, text ="Afficher tout les contacte du répertoir", relief=RAISED, command=self._afficher_all_contact)
        self.b5 = Button(root, text ="Génerer un contatct aléatoir", relief=RAISED, command=self._generer)
        self.b6 = Button(root, text ="Confirmer", relief=RAISED, command=self.__confirme)

        #coller a la fennetre
        self.label.place(x=300,y=10)
        self.entry.place(x=300,y=100,width=450,height=450)
        self.b1.place(x=175,y=100)
        self.b2.place(x=178,y=150)
        self.b3.place(x=188,y=200)
        self.b4.place(x=100,y=250)
        self.b5.place(x=150,y=300)
        self.b6.place(x=500,y=100)

    def __confirme(self):
        self.saisie = self.text_var.get()
        if self.rechercher:
           self.text_var.set(self.repertoir.rechercher_contact(nom=self.saisie))
           self.rechercher = False
        elif self.supprimer:
            self.repertoir.supprimer_contact(nom=self.saisie)
            self.supprimer = False
        elif self.afficherall:
            self.text_var.set(self.repertoir.afficher_repertoire())
            self.afficherall = False
        elif self.generer:
            self.text_var.set(self.repertoir.randome_contact())
            self.generer =  False
        elif self.ajouter:
            concernant = self.saisie.split(',')
            self.repertoir.ajouter_contact(nom=concernant[0], prenom=concernant[1], numero=concernant[3])
            self.ajouter = False
        elif self.modifier:
            a_modifier = self.saisie.split(':')
            new = a_modifier[1].split(',')
            self.repertoir.modifier_contact(nom=a_modifier[0], new_nom=new[0], new_prenom=new[1], new_numero=new[2])
            self.modifier = False
    def _rechercher(self):
        self.rechercher = True
        self.text_var.set('saisisez le nom de votre contact après avoir supprimer ce message!')
    
    def _supprimer(self):
        self.rechercher = True
        self.text_var.set('saisissez le nom de votre contact après avoir supprimer ce message!')
    
    def _afficher_all_contact(self):
        self.afficherall = True

    def _generer(self):
        self.generer = True

    def _ajouter(self):
        self.ajouter = True
        self.text_var.set('Sausissez les information de la fçon suivante:nom,prenom,numéro.A près avoir supprimer ce message!')
    
    def _modifier(self):
        self.modifier = True
        self.text_var.set('nom:nouveau nom, nouveau prenom, nouveau numéro (les élement doivent être saisie*')
        
    def mainloop(self):
        self.root.mainloop()

def main():
    root = tk.Tk()
    app = App(root)
    app.mainloop()


if __name__ == '__main__':
    main()

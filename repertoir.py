#!/usr/bin/env python3
# -*- coding: utf-8 -*-

####IMPORTATION####
from tkinter import*
import csv
import random

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
class App(Frame):

    '''class App qui hérite de la class Frame du module tkinter, crée une fenêtre GUI
    '''

    def __init__(self, root):
        super().__init__(root)
    def fenetre(self):
        pass
    
    def mainloop(self):
        mainloop()

def main():
    mon_repertoire =  Repertoire()
    nouveau_contact = mon_repertoire.randome_contact()
    print(nouveau_contact)

if __name__ == '__main__':
    main()

# -*- encoding: utf-8 -*-

'''
    Regroupe l'ensemble des fonctions utile à nôtre répertoire téléphonique.
    Les fonctions sont les suiventes:
        - lecture : permet de lire dans le répertoire pour retrouver un contact ou afficher tout les contacts.
        - ecriture : permet d'écrire dans le répertoire pour crée un nouveau contact.
        - import : permet d'importer des contacts
'''

import csv

def lecture(return_all:bool, nom=None, prenom=None):
    ''' lecture : permet de lire dans le répertoire pour retrouver un contacte ou afficher tout les contacts.
        IN:
            return_all : paramétre de la fonction lecture (valeur par défaut=aucun, type=bool)
            nom : paramétre de la fonction lecture (valeur par défaut=None, type=str) nom contact
            prenom : paramétre de la fonction lecture (valeur par défaut=None, type=str) prénom contact
        OUT:
            Si return_all == True alors:
                il retourne tout le répertoire (trié dans l'ordre alphabétique)
            Sinon si return_all == False alors:
                il retourne le contact correspondant au nom et au prénom des variable nom prenom si il existe:
                sinon il retourne False
    '''
    def get_nom(contact):
        return contact['nom']

    assert type(return_all) == bool
    if return_all:
        with open('repertoire.csv', 'r', encoding='utf-8') as fichier:
            contacts = [dict(contact) for contact in csv.DictReader(fichier)]
            contacts.sort(key=get_nom)
        return contacts
    else:
        assert type(nom) == str
        assert type(prenom) == str
        with open('repertoire.csv', 'r', encoding='utf-8') as fichier:
            contacts = [dict(contact) for contact in csv.DictReader(fichier)]
        for contact in contacts:
            if contact['nom'] == nom.upper() and contact['prenom'] == prenom.title():
                return contact
        else:
            return False

def ecriture(nom:str, prenom:str, telephone:str):
    ''' ecriture : permet d'écrire dans le répertoire pour crée un nouveau contact.
        IN:
            nom: paramétre de la fonction ecriture (valeur par défaut=aucun, type=str) nom contact
            prenom: paramétre de la fonction ecriture (valeur par défaut=aucun, type=str) prenom contact
                condition pour le prénom:
                    - Si plusieurs prenoms doit être séparer par un espace.
            telephone: paramétre de la fonction ecriture (valeur par défaut=aucun, type=str) numéro contact
                conditions pour le numéro:
                    - Doit contenir 10 chiffres.
                    - Doit commencer par '06', ou '07',ou '02'.
        OUT:
            Enregistre le contact sous la forme [nom,prenom,telephone] dans le fichier repertoire.csv
            retourne False si les condition pour le numéro ne sont pas respecter!
        test:
        -----
        >>>contact = fonction.lecture(False, 'Contact', 'test')
        >>>assert contact == {'nom':'CONTACT', 'prenom':'Test', 'telephone':'0639058698'}
        (les )
    '''
    assert type(nom) == str
    assert type(prenom) == str
    assert type(telephone) == str
    try:
        int(telephone)
    except ValueError:
        return False
    if not telephone[:2] in ['06','07','02'] or len(telephone) != 10:
        return False
    with open('repertoire.csv', 'a', encoding='utf-8', newline='') as fichier:
        writer = csv.writer(fichier, delimiter=',')
        writer.writerow([nom.upper(),prenom.title(),telephone])
        return True

def importation(fichier_user:str):
    ''' import : permet d'importer des contacts
        IN:
            fichier: paramétre de la fonction import_file (valeur par défaut=aucun, type=str) ficher
        OUT:
            Transfert les contacts du répertoire dans le fichier de l'utilisateur.
    '''
    assert type(fichier_user) == str
    with open(fichier_user, 'r', encoding='utf-8') as fichier:
        contacts = [dict(contact) for contact in csv.DictReader(fichier)]
    with open('repertoire.csv', 'a', encoding='utf-8', newline='') as fichier:
        writer = csv.writer(fichier, delimiter=',')
        if list(contacts[0].keys()) == ['nom', 'prenom', 'telephone']:
            for contact in contacts:
                writer.writerow([contact['nom'].upper(), contact['prenom'].title(), contact['telephone']])
        else:
            return False
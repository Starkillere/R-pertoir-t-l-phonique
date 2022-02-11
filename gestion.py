import sqlite3
import csv


con = sqlite3.connect('contact.bd')
cursor = con.cursor()

#Table
"""
cursor.execute('''CREATE TABLE user (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nom TEXT NOT NULL,
                  prenom TEXT NOT NULL,
                  telephone TEXT NOT NULL
           );''')
"""

def get_contact(return_all:bool, nom=None, prenom=None):
    assert type(return_all) == bool
    requete = 'select * from user'
    if return_all:
        contacts = cursor.execute(requete)
        return contacts
    else:
        assert type(nom) == str
        assert type(prenom) == str
        contacts = cursor.execute(requete)
        if ' ' in prenom:
            cap_prenom = ''
            for i in range(len(prenom.split(' '))):
                cap_prenom += ((prenom.split(' '))[i]).capitalize() + ' '
            prenom = cap_prenom.strip()
        else:
            prenom = prenom.capitalize()
        for contact in contacts:
            if contact[1] == nom.upper() and contact[2] == prenom:
                con.close()
                return contact
        else:
            con.close()
            return False
    

def creat_contact(nom:str, prenom:str, telephone:str):
    assert type(nom) == str
    assert type(prenom) == str
    assert type(telephone) == str
    try:
        int(telephone)
    except ValueError:
        return False
    if not telephone[:2] in ['06', '02', '07'] or len(telephone) != 10:
        return False
    if ' ' in prenom.strip():
        cap_prenom = ''
        for i in range(len(prenom.split(' '))):
            cap_prenom += ((prenom.split(' '))[i]).capitalize() + ' '
        prenom = cap_prenom.strip()
    else:
        prenom = prenom.capitalize()
    requete = "insert into user (nom, prenom, telephone) values ('{nom}', '{prenom}', '{telephone}'".format(nom.upper(), prenom, telephone)
    cursor.execute(requete)

    con.commit()
    con.close()
    return True

def import_contact(fichier_user):
    assert type(fichier_user) == str
    with open(fichier_user, 'r', encoding='utf-8') as fichier:
        contacts = [dict(contact) for contact in csv.DictReader(fichier)]
    if contacts[0].keys() == ['nom', 'prenom', 'telephone']:
        for contact in contacts:
            if ' ' in contact['prenom'].strip():
                cap_prenom = ''
                for i in range(len(contact['prenom'].split(' '))):
                    cap_prenom += ((contact['prenom'].split(' '))[i]).capitalize() + ' '
                contact['prenom'] = cap_prenom.strip()
            else:
                contact['prenom'] = contact['prenom'].capitalize()
            requete = "insert into user (nom, prenom, telephone) values ('{nom}', '{prenom}', '{telephone}'".format(contact['nom'].upper(), contact['prenom'], contact['telephone'])
            cursor.execute(requete)

    con.commit()
    con.close()
    return True
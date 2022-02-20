import sqlite3
import csv

#Table
"""
con = sqlite3.connect('contact.bd')
cursor = con.cursor()
cursor.execute('''CREATE TABLE user (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nom TEXT NOT NULL,
                  prenom TEXT NOT NULL,
                  telephone TEXT NOT NULL
           );''')
con.commit()
con.close()
"""
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
        return contact[1]
    con = sqlite3.connect('contact.bd')
    cursor = con.cursor()
    assert type(return_all) == bool
    requete = 'select * from user'
    if return_all:
        contacts = cursor.execute(requete)
        contacts = list(contacts)
        contacts.sort(key=get_nom)
        return contacts
    else:
        assert type(nom) == str
        assert type(prenom) == str
        contacts = cursor.execute(requete)
        for contact in contacts:
            if contact[1] == nom.upper() and contact[2] == prenom.title():
                con.close()
                return contact
        else:
            con.close()
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
            Enregistre le contact sous la forme [nom,prenom,telephone] dans le fichier contact.db table user
            retourne False si les condition pour le numéro ne sont pas respecter!
        test:
        -----
        >>>contact = fonction.lecture(False, 'Contact', 'test')
        >>>assert contact == ('CONTACT','Test','0639058698'}
        (les )
    '''
    con = sqlite3.connect('contact.bd')
    cursor = con.cursor()
    assert type(nom) == str
    assert type(prenom) == str
    assert type(telephone) == str
    try:
        int(telephone)
    except ValueError:
        return False
    if not telephone[:2] in ['06', '02', '07'] or len(telephone) != 10:
        return False
    requete = "insert into user (nom, prenom, telephone) values('{nom}', '{prenom}', '{telephone}')".format(nom = nom.upper(),prenom = prenom.title(),telephone= telephone)
    cursor.execute(requete)

    con.commit()
    con.close()
    return True

def importation(fichier_user):
    ''' import : permet d'importer des contacts
        IN:
            fichier: paramétre de la fonction import_file (valeur par défaut=aucun, type=str) ficher
        OUT:
            Transfert les du fichier de l'utilisateur dans le repertoir.
    '''
    con = sqlite3.connect('contact.bd')
    cursor = con.cursor()
    assert type(fichier_user) == str
    with open(fichier_user, 'r', encoding='utf-8') as fichier:
        contacts = [dict(contact) for contact in csv.DictReader(fichier)]
    if list(contacts[0].keys()) == ['nom', 'prenom', 'telephone']:
        for contact in contacts:
            requete = "insert into user (nom, prenom, telephone) values ('{nom}', '{prenom}', '{telephone}') ".format(nom = contact['nom'].upper(), prenom = contact['prenom'].title(), telephone = contact['telephone'])
            cursor.execute(requete)
    else:
       return False

    con.commit()
    con.close()
    return True

if __name__ == '__main__':
    con = sqlite3.connect('contact.bd')
    cursor = con.cursor()
    cursor.execute('DELETE FROM user WHERE id != 1')
    con.commit()
    con.close()
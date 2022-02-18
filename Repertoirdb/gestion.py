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
def lecture(return_all:bool, nom=None, prenom=None):
    assert type(return_all) == bool
    requete = 'select * from user'
    if return_all:
        contacts = cursor.execute(requete)
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
    assert type(nom) == str
    assert type(prenom) == str
    assert type(telephone) == str
    try:
        int(telephone)
    except ValueError:
        return False
    if not telephone[:2] in ['06', '02', '07'] or len(telephone) != 10:
        return False
    requete = "insert into user (nom, prenom, telephone) values ('{nom}', '{prenom}', '{telephone}')".format(nom = nom.upper(),prenom = prenom.title(),telephone= telephone)
    cursor.execute(requete)

    con.commit()
    con.close()
    return True

def importation(fichier_user):
    assert type(fichier_user) == str
    with open(fichier_user, 'r', encoding='utf-8') as fichier:
        contacts = [dict(contact) for contact in csv.DictReader(fichier)]
    if list(contacts[0].keys()) == ['nom', 'prenom', 'telephone']:
        for contact in contacts:
            requete = "insert into user (nom, prenom, telephone) values ('{nom}', '{prenom}', '{telephone}')".format(nom = contact['nom'].upper(), prenom = contact['prenom'].title(), telephone = contact['telephone'])
            cursor.execute(requete)
    else:
        print("Mince")

    con.commit()
    con.close()
    return True

if __name__ == "__main__":
    import unittest
    class Test(unittest.TestCase):

        def test_recherche(self):
            contact = lecture(False, 'GOLDSTEIN', 'Pina')
            self.assertEqual(contact, ('GOLDSTEIN','Pina','0634267174'))
            self.assertEqual(lecture(False, "N'existe", 'Pas'), False)

        def test_importation(self):
            importation('fake.csv')
            contacts =  lecture(True)
            self.assertEqual(list(contacts)[-1], ('SCHIAVONE','Gaspare','0628691748'))

    unittest.main()
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
import fonction
import unittest

class Test(unittest.TestCase):

    def test_recherche(self):
        contact = fonction.lecture(False, 'Contact', 'test')
        self.assertEqual(contact, {'nom':'CONTACT', 'prenom':'Test', 'telephone':'0639058698'})
        self.assertEqual(fonction.lecture(False, "N'existe", 'Pas'), False)

    def test_importation(self):
        fonction.importation('jojo.csv')
        contacts =  fonction.lecture(True)
        self.assertEqual(contacts[-1], {'nom':'CONTACT', 'prenom':'Test Ii', 'telephone':'0645789856'})

if __name__ == '__main__':
    unittest.main()

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
import fonction
import unittest

class Test(unittest.TestCase):

    def test_recherche(self):
        contact = fonction.lecture(False, 'TEST', 'test')
        self.assertEqual(contact, {'nom':'TEST', 'prenom':'Test', 'telephone':'0639058698'})
        self.assertEqual(fonction.lecture(False, "N'existe", 'Pas'), False)

    def test_importation(self):
        try:
            fonction.importation('fake.csv')
        except FileNotFoundError:
            fonction.importation('test\\fake.csv')
        contacts =  fonction.lecture(True)
        self.assertEqual(contacts[-1], {'nom': 'ÉTIENNE-SALMON', 'prenom': 'Raymond', 'telephone': '0790274211'})

if __name__ == '__main__':
    import csv
    def getParent(path: str, levels=1) -> str:
        """
        @param path: starts without /
        @return: Parent path at the specified levels above.
        """
        current_directory = os.path.dirname(__file__)

        parent_directory = current_directory
        for i in range(0, levels):
            parent_directory = os.path.split(parent_directory)[0]

        file_path = os.path.join(parent_directory, path)
        return file_path
  
    datas_1 = {'nom':'TEST', 'prenom':'Test', 'telephone':'0639058698'}
    with open(getParent('repertoire.csv'),'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["nom", "prenom", "telephone"])
        writer.writeheader()
        writer.writerow(datas_1)
    unittest.main()
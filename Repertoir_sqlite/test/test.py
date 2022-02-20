
import sqlite3
import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
import gestion 

class Test(unittest.TestCase):
    def test_recherche(self):
        contact = gestion.lecture(False, 'TEST', 'Test')
        self.assertEqual(contact, (1,'TEST','Test','0636068103'))
        self.assertEqual(gestion.lecture(False, "N'existe", 'Pas'), False)
        
    def test_importation(self):
        try:
            gestion.importation('fake.csv')
        except FileNotFoundError:
            gestion.importation('test\\fake.csv')
        contacts =  gestion.lecture(True)
        contact = list(contacts)[-1]
        self.assertEqual((contact[1], contact[2], contact[3]),('ÉTIENNE-SALMON', 'Raymond', '0790274211'))

if __name__ == '__main__':
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
    con = sqlite3.connect(getParent('contact.bd'))
    cursor = con.cursor()
    cursor.execute('DELETE FROM user WHERE id != 1')
    con.commit()
    con.close()
    unittest.main()
    

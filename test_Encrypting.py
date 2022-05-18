import unittest
from Encrypting import *

class test_Encrypting(unittest.TestCase):
    def test_encriptar(self):
        #Validar que la encriptacion y desencriptación funcionen
        self.assertEqual('Hola', desencriptar(encriptar('Hola')))

if __name__=='__main__':
    unittest.main()

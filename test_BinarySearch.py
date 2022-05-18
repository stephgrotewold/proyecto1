import unittest
from BinarySearch import *
from LecturaArchivoTexto import Leer, Leer_clientes
productos=[]
clients=[]
Leer_clientes(clients)
Leer(productos)

class test_BinarySearch(unittest.TestCase):
    def test_binarySearch(self):
        #Validar que el item haya sido encontrado
        self.assertEqual(productos[0], binarySearch(productos, 1101))
        #Validar que el item no haya sido encontrado
        self.assertEqual(None, binarySearch(productos, 165263))

    def test_binarySearch_clientes(self):
        #Validar que el numero haya sido encontrado
        self.assertEqual(clients[0], binarySearch_clientes(clients, 1792))
        #Validar que el numero no haya sido encontrado
        self.assertEqual(0, binarySearch_clientes(clients, 8468469))


if __name__=='__main__':
    unittest.main()

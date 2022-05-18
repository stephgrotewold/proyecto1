import unittest
from Queue import *

class test_Queue(unittest.TestCase):
    def test_enqueue(self):
        #Verificar que se ingrese en la queue
        ordenes=[]
        enqueue(ordenes, 'Esteban', 'Zona16', '35351054')
        self.assertEqual(1,len(ordenes))
    
    def test_dequeue(self):
        #Verificar que se realiza el dequeue
        ordenes=[{'nombre': 'Esteban', 'direccion': 'Zona16', 'numero': 35351054}]
        dequeue(ordenes)
        self.assertEqual(0, len(ordenes))
    
    def test_IsEmpty(self):
        #Verifiar que la cola se encuentra vacia
        ordenes=[]
        self.assertEqual(True, IsEmpty(ordenes))

    def test_Empty(self):
        #Verificar que se vacíe la cola
        ordenes=[{'nombre': 'Esteban', 'direccion': 'Zona16', 'numero': 35351054},{'nombre': 'Josue', 'direccion': 'Mixco', 'numero': 35351055}]
        Empty(ordenes)
        self.assertEqual(0,len(ordenes))


    

if __name__=='__main__':
    unittest.main()

import unittest
from Queue import days_between, elim_vencidos, pop_item, vencidos
from datetime import datetime
from LecturaArchivoTexto import productos
productos1 = productos.copy()

class test_Queue(unittest.TestCase):
    def test_days_between(self):
        #Validar la diferencia de días
        self.assertEqual(1, days_between('2022-05-05 00:00:00'))

    def test_vencidos(self):
        prueba=[{'caducidad':datetime.strptime('03-03-2023', '%d-%m-%Y')}]
        #Validar cuando no se encuentra ningun producto vencido
        self.assertEqual(0, vencidos(prueba))
    
    def test_elim_vencidos(self):
        prueba=[{'caducidad':datetime.strptime('03-03-2023', '%d-%m-%Y')}]
        #Validar cuando no se encuentra ningun producto vencido 
        self.assertEqual(0,elim_vencidos(prueba))
        prueba=[]
        #Validar cuando no hay ningun producto vencido
        self.assertEqual(0,elim_vencidos(prueba))

    def test_pop_item(self):
        prueba=[]
        #Validar cuando el array esta vacío
        self.assertEqual(0,pop_item(prueba))

    

if __name__=='__main__':
    unittest.main()

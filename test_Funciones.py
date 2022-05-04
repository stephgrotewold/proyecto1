import unittest
from Funciones import *
from LecturaArchivoTexto import productos
productos_carrito=[]
productos1 = productos.copy()

class Test_Funciones(unittest.TestCase):
    def test_sum_cantidad(self):
        # Validar error cuando no se ingresan enteros
        self.assertRaises(TypeError, sum_cantidad, 'a', 'b', productos)
        # Validar que se sume la cantidad
        self.assertEqual(1, sum_cantidad(1503,5, productos))
        # Validar error cuando no se encuentra el ID
        self.assertEqual(0, sum_cantidad(1452,7,productos))
    
    def test_rest_cantidad(self):
        # Validar error cuando no se ingresan enteros
        self.assertRaises(TypeError, rest_cantidad, 'a', 'b', productos)
        # Validar que se reste la cantidad
        self.assertEqual(1, rest_cantidad(1503,5, productos))
        # Validar error cuando no hay suficiente cantidad en el inventario
        self.assertEqual(0, rest_cantidad(1205,200, productos))
        # Validar error cuando no se encuentra el ID
        self.assertEqual(0, rest_cantidad(1582,7,productos))
    
    def test_edit_name(self):
        # Validar error cuando no se ingresan enteros
        self.assertRaises(TypeError, edit_name, 'hola', 'Pollo', productos)
    
    def test_edit_precio(self):
        # Validar error cuando no se ingresan enteros
        self.assertRaises(TypeError, edit_precio, 'c', 'ñ', productos)
        # Validar que se edite el precio
        self.assertEqual(1,edit_precio( 1411, 40, productos))
        # Validar error cuando no se encuentra el ID
        self.assertEqual(0,edit_precio( 1251, 40, productos))

    def test_edit_cant(self):
        # Validar error cuando no se ingresan enteros
        self.assertRaises(TypeError, edit_cant, 'a', 'b', productos)
        # Validar que se edite la cantidad
        self.assertEqual(1, edit_cant(1702,20, productos))
        # Validar error cuando no se encuentra el ID
        self.assertEqual(0,edit_cant( 1151, 40, productos))

    def test_elim_item(self):
        # Validar error cuando no se ingresan enteros
        self.assertRaises(TypeError, elim_item, 'ñ', productos)
        # Validar que se elimine el item
        self.assertEqual(1, elim_item(1310, productos))
        # Validar error cuando no se encuentra el ID
        self.assertEqual(0, elim_item(1919, productos))
    
    def test_search_name(self):
        #Validar que se encuentre la base de datos
        self.assertEqual(1,search_name('Tomate',productos))
        #Validar error cuando no se encuentra la base de datos
        self.assertEqual(0,search_name('PS4',productos))
    
    def test_verify_name(self):
        # Validar error cuando la cantidad no es un entero
        self.assertRaises(TypeError, verify_name, 'Escoba', 'cuatro', productos)
        # Validar que se encuentre el ID
        self.assertEqual(1103, verify_name('Jugo', 4, productos))
        # Validar error cuando no se encuentra el ID
        self.assertEqual(0, verify_name('Pizza', 6, productos))
    
    def test_total(self):
        # Validar error cuando la cantidad no es un entero
        self.assertRaises(TypeError, total, 'XL', 'k', productos)
        # Validar que retorna el total
        self.assertEqual(18, total('Escoba', 2, productos))
    
    def test_search_carrito(self):
        # Validar que el item se encuentre en el carrito
        productos_carrito.append({'item_name': 'Lomito', 'cantidad':2})
        self.assertEqual(1,search_carrito('Lomito',productos_carrito))
        # Validar error que el item no se encuentre en el carrito
        self.assertEqual(0,search_carrito('Shampoo',productos_carrito))

    def test_search_cant(self):
        # Validar que retorne la cantidad
        productos_carrito.append({'item_name': 'Tomate', 'cantidad':4 })
        self.assertEqual(4,search_cant('Tomate',productos_carrito))

    def test_positivo(self):
        # Validar que ingrese un entero
        self.assertRaises(TypeError, positivo, 'a')
        # Validar un numero positivo
        self.assertEqual(1,positivo(2))
        # Validar un numero negativo
        self.assertEqual(0,positivo(-2))
    

    def test_reparar(self):
        self.assertEqual(1,reparar(productos1))
    


if __name__=='__main__':
    unittest.main()



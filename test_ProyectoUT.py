import unittest
import Proyecto
from Proyecto import sum_cantidad
from Proyecto import rest_cantidad
from Proyecto import edit_name
from Proyecto import edit_precio
from Proyecto import edit_cant
from Proyecto import elim_item
from Proyecto import verify_name
from Proyecto import search_id
from Proyecto import total
from Proyecto import saldar
from Proyecto import search_carrito
from Proyecto import search_cant
from Proyecto import positivo
class TestProyecto(unittest.TestCase):
    def test_sum_cantidad(self):
        # Validar error cuando no se ingresan enteros
        self.assertRaises(TypeError, sum_cantidad, 'a', 'b', Proyecto.item_database_alcohol)
        # Validar que se sume la cantidad
        self.assertEquals(1, Proyecto.sum_cantidad(1503,5, Proyecto.item_database_hogar))
        # Validar error cuando no se encuentra el ID
        self.assertEquals(0, Proyecto.sum_cantidad(1402,7,Proyecto.item_database_panaderia))

    def test_rest_cantidad(self):
        # Validar error cuando no se ingresan enteros
        self.assertRaises(TypeError, rest_cantidad, 'a', 'b', Proyecto.item_database_bebidas)
        # Validar que se reste la cantidad
        self.assertEquals(1, Proyecto.rest_cantidad(1303,3, Proyecto.item_database_panaderia))
        # Validar error cuando no hay suficiente cantidad en el inventario
        self.assertEquals(0, Proyecto.rest_cantidad(1205,200, Proyecto.item_database_carnes))
        # Validar error cuando no se encuentra el ID
        self.assertEquals(0, Proyecto.rest_cantidad(1502,7,Proyecto.item_database_panaderia))

    def test_edit_name(self):
        # Validar error cuando no se ingresan enteros
        self.assertRaises(TypeError, edit_name, 'hola', 'Pollo', Proyecto.item_database_carnes)
        # Validar que se edite el nombre
        self.assertEquals(1,Proyecto.edit_name(1105, 'Mountain Dew', Proyecto.item_database_bebidas))
        # Validar error cuando no se encuentra el ID
        self.assertEquals(0,Proyecto.edit_name(1505, 'Mountain Dew', Proyecto.item_database_bebidas))

    def test_edit_precio(self):
        # Validar error cuando no se ingresan enteros
        self.assertRaises(TypeError, edit_precio, 'c', 'ñ', Proyecto.item_database_frutas_verduras)
        # Validar que se edite el precio
        self.assertEquals(1,Proyecto.edit_precio( 1411, 40, Proyecto.item_database_frutas_verduras))
        # Validar error cuando no se encuentra el ID
        self.assertEquals(0,Proyecto.edit_precio( 1201, 40, Proyecto.item_database_panaderia))

    def test_edit_cant(self):
        # Validar error cuando no se ingresan enteros
        self.assertRaises(TypeError, edit_cant, 'a', 'b', Proyecto.item_database_carnes)
        # Validar que se edite la cantidad
        self.assertEquals(1, Proyecto.edit_cant(1702,20, Proyecto.item_database_alcohol))
        # Validar error cuando no se encuentra el ID
        self.assertEquals(0,Proyecto.edit_cant( 1001, 40, Proyecto.item_database_panaderia))

    def test_elim_item(self):
        # Validar error cuando no se ingresan enteros
        self.assertRaises(TypeError, elim_item, 'ñ', Proyecto.item_database_bebidas)
        # Validar que se elimine el item
        self.assertEquals(1, Proyecto.elim_item(1310, Proyecto.item_database_panaderia))
        # Validar error cuando no se encuentra el ID
        self.assertEquals(0, Proyecto.elim_item(1910, Proyecto.item_database_hogar))

    def test_search_id(self):
        # Validar error cuando no se ingresan enteros
        self.assertRaises(TypeError, search_id, 'Baygon')
        # Validar que se encuentre la base de datos
        self.assertEquals(Proyecto.item_database_hogar, Proyecto.search_id(1505))
        # Validar error cuando no se encuentra la base de datos
        self.assertEquals(0,Proyecto.search_id(150))
    def test_search_name(self):
        #Validar que se encuentre la base de datos
        self.assertEquals(Proyecto.item_database_frutas_verduras,Proyecto.search_name('Tomate'))
        #Validar error cuando no se encuentra la base de datos
        self.assertEquals(0,Proyecto.search_name('PS4'))

    def test_verify_name(self):
        # Validar error cuando la cantidad no es un entero
        self.assertRaises(TypeError, verify_name, 'Escoba', 'cuatro', Proyecto.item_database_hogar)
        # Validar que se encuentre el ID
        self.assertEquals(1104, Proyecto.verify_name('Jugo de Manzana', 4, Proyecto.item_database_bebidas))
        # Validar error cuando no se encuentra el ID
        self.assertEquals(0, Proyecto.verify_name('Pescado', 6, Proyecto.item_database_bebidas))

    def test_total(self):
        # Validar error cuando la cantidad no es un entero
        self.assertRaises(TypeError, total, 'XL', 'k', Proyecto.item_database_alcohol)
        # Validar que retorna el total
        self.assertEquals(18, Proyecto.total('Escoba', 2, Proyecto.item_database_hogar))

    def test_total(self):
        # Validar error cuando la cantidad no es un entero
        self.assertRaises(TypeError, saldar, 'Pan de especies', 'seis', Proyecto.item_database_panaderia)

    def test_search_carrito(self):
        # Validar que el item se encuentre en el carrito
        Proyecto.item_database_carrito.append({'item_name': 'Lomito', 'cantidad':2, 'pasillo':Proyecto.item_database_carnes })
        self.assertEquals(1,search_carrito('Lomito'))
        # Validar error que el item no se encuentre en el carrito
        self.assertEquals(0,search_carrito('Shampoo'))
    def test_search_cant(self):
        # Validar que retorne la cantidad
        Proyecto.item_database_carrito.append({'item_name': 'Tomate', 'cantidad':4, 'pasillo':Proyecto.item_database_frutas_verduras })
        self.assertEquals(4,search_cant('Tomate'))
    def test_positivo(self):
        # Validar que ingrese un entero
        self.assertRaises(TypeError, positivo, 'a')
        # Validar un numero positivo
        self.assertEquals(1,positivo(2))
        # Validar un numero negativo
        self.assertEquals(0,positivo(-2))

if __name__=='__main__':
    unittest.main()

import cProfile
from Funciones import *
from LecturaArchivoTexto import Leer
productos=[]
Leer(productos)
cProfile.run('sum_cantidad(1702,5,productos)')
cProfile.run('rest_cantidad(1702,5,productos)')
cProfile.run('elim_item(1702,productos)')
cProfile.run('edit_name(1704,"Indita",productos)')
cProfile.run('edit_precio(1503,40,productos)')
cProfile.run('edit_cant(1402,30,productos)')
cProfile.run('search_name("Pollo", productos)')
cProfile.run('verify_id(1702,productos)')
cProfile.run('verify_name(1703, 2,productos)')
cProfile.run('total("XL",2,productos)')
cProfile.run('saldar("Leche", 5, productos)')
cProfile.run('search_carrito("Gallo",productos)')
cProfile.run('search_cant("Pan_de_agua",productos)')
cProfile.run('positivo(2)')

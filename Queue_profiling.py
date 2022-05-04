import cProfile
from Queue import days_between, elim_vencidos, pop_item, vencidos
from LecturaArchivoTexto import productos
from Funciones import reparar
productos1=productos.copy()
cProfile.run('days_between("2022-05-05 00:00:00")')
cProfile.run('vencidos(productos)')
cProfile.run('elim_vencidos(productos)')
cProfile.run('pop_item(productos)')
reparar(productos1)
import cProfile
from BinarySearch import  *
from LecturaArchivoTexto import Leer, Leer_clientes
products=[]
clients=[]
Leer_clientes(clients)
Leer(products)
cProfile.run('binarySearch(products,1101)')
cProfile.run('binarySearch_clientes(clients, 35351054)')
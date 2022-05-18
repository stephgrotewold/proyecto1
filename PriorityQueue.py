from Funciones import days_between
from LecturaArchivoTexto import Leer, actualizar
def heapify(arr, n, i):
    largest = i #root
    l = 2 * i + 1#left
    r = 2 * i + 2#right

    #Revisar si left child existe y si es mayor que la raiz
    if l < n and days_between(str(arr[i]['caducidad'])) < days_between(str(arr[l]['caducidad'])):
        largest = l
  
    # Revisar si right child existe y si es mayor que la raiz
    if r < n and days_between(str(arr[largest]['caducidad'])) < days_between(str(arr[r]['caducidad'])):
        largest = r
  
    # Cambiar raiz si es necesario
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
  
        # Heapify la raiz
        heapify(arr, n, largest)
  

def heapSort(arr,n):
  
    # Hacer un maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
  
    # Sacar los elementos
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)

#Revisa si el queue esta vacío
def IsEmpty(self):
    return len(self) == 0

#Elimina la primera posicion de la priority queue
def elim_head():
    arr=[]
    Leer(arr)
    heap(arr)
    if not IsEmpty(arr):
        arr.pop(0)
        actualizar(arr)

#Elimina los primeros elementos de la priority queue, revisando si el pimero esta vencido
def elim_vencidos():
    arr=[]
    Leer(arr)
    heap(arr)
    while not IsEmpty(arr) and days_between(str(arr[0]['caducidad']))<0:
        arr.pop(0)
    actualizar(arr)

#Imprime los elementos vencidos de la priority queue
def print_vencidos():
    arr=[]
    Leer(arr)
    heap(arr)
    cont=0
    while not IsEmpty(arr) and days_between(str(arr[cont]['caducidad']))<0:
        print('Nombre: '+ arr[cont]['item_name'] + ' Fecha de caducidad: ' + arr[cont]['caducidad']+ '\n' ) 
        cont+=1
    if not IsEmpty(arr):
        print('No hay ningun item vencido')

#Conversion del array a un heap
def heap(arr):
    n = len(arr)
    heapSort(arr,n)

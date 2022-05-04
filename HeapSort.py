from LecturaArchivoTexto import productos
from datetime import datetime
from Queue import days_between
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
        
def sort(arr):
    n = len(arr)
    heapSort(arr,n)

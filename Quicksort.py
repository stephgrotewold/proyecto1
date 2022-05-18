# Quicksort
# funcion para encontrar la particion
def partition(array, low, high):

  # Elige el mas hacia la derecha como pivot
  pivot = array[high]['item_id']

  # pointer al elemento mas grande
  i = low - 1

  # traverse a los elementos
  # Compara los elementos con el pivot
  for j in range(low, high):
    if array[j]['item_id'] <= pivot:
      # Si el elemento encontrado es menor que el pivot
      # Cambiar el elemento con el i
      i = i + 1

      # Cambio del elemento de i con el de j
      (array[i], array[j]) = (array[j], array[i])

  # Cambia el pivot con el elemento guardado en i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # regresa cuando la particion esta completa
  return i + 1

# Funcion para usar Quicksort
def quickSort(array, low, high):
  if low < high:

    # Encuentra el pivot de manera que
    # los elementos menores que el pivot estan a la izq
    # Elementos mas grandes que el pivot estan a la der
    pi = partition(array, low, high)

    # Recursion del pivot del lado izq
    quickSort(array, low, pi - 1)

    # Recursion del pivot del lado der
    quickSort(array, pi + 1, high)
        
def sort(arr):
    n = len(arr)-1
    quickSort(arr,0,n)



def partition_clientes(array, low, high):

  # Escoge el elemento que esta mas a la derecha como pivot
  pivot = array[high]['numero']

  # pointer a uno mayor
  i = low - 1

  # traverse a los elementos
  # compara los elementos con el pivot
  for j in range(low, high):
    if array[j]['numero'] <= pivot:
      # si encuentra un elemento menor que el pivot
      # lo intercambia con el mayor guardado en i
      i = i + 1

      # cambia el elemento de i con el de j
      (array[i], array[j]) = (array[j], array[i])

  # cambia el pivot con el elemento mayor guardado en i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # regresa la particion cuando termina
  return i + 1

# funcion de quicksort con clientes
def quickSort_clientes(array, low, high):
  if low < high:

    # Encuentra el pivot de manera que
    # los elementos menores que el pivot estan a la izq
    # Elementos mas grandes que el pivot estan a la der
    pi = partition_clientes(array, low, high)

    # Recursion del pivot del lado izq
    quickSort_clientes(array, low, pi - 1)

    # Recursion del pivot del lado der
    quickSort_clientes(array, pi + 1, high)

def sort_clientes(arr):
    n=len(arr)-1
    quickSort_clientes(arr, 0,n)
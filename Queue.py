from datetime import datetime
from datetime import date
from LecturaArchivoTexto import productos
from LecturaArchivoTexto import actualizar
from Funciones import elim_item
#Calcula la diferencia de días entre la fecha de caducidad y hoy
def days_between(d2):
    d1 = datetime.today()
    d2 = datetime.strptime(d2, '%Y-%m-%d %H:%M:%S')
    return (d2 - d1).days+1


#Muestra los items que ya están vencidos
def vencidos(arr):
    flag=0
    for i in arr:
        if days_between(str(i['caducidad']))<=0:
            flag=1
            print(i)
    if flag==0:
        return 0

#Elimina los items que ya están vencidos
def elim_vencidos(arr):
    flag=0
    while(len(arr)>0 and days_between(str(arr[0]['caducidad']))<=0):
        if (elim_item(arr[0]['item_id'], productos) == 1):
            print('Item eliminado con exito')  
            arr.pop(0)
            flag=1
            actualizar()
    if flag==0:
        return 0

#Elimina el primero elemento del queue
def pop_item(arr):
    if (len(arr) >0 and elim_item(arr[0]['item_id'], productos) == 1):
        print('Item eliminado con exito')
        arr.pop(0)
    else:
        return 0

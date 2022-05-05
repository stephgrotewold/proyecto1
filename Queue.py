from datetime import datetime
from datetime import date
from LecturaArchivoTexto import productos
from LecturaArchivoTexto import actualizar
from Funciones import elim_item
from rich.console import Console
from rich.theme import Theme
from rich.table import Table

custom_theme = Theme({"success": "green", "error": "bold red"})
console = Console(theme=custom_theme)


#Calcula la diferencia de días entre la fecha de caducidad y hoy
def days_between(d2):
    d1 = datetime.today()
    d2 = datetime.strptime(d2, '%Y-%m-%d %H:%M:%S')
    return (d2 - d1).days+1


#Muestra los items que ya están vencidos
def vencidos(arr):
    flag=0
    table_vencido = Table(title='PRODUCTOS VENCIDOS')
    table_vencido.add_column("item_id", style="bold")
    table_vencido.add_column("item_name", style="bold")
    table_vencido.add_column("precio", style="bold")
    table_vencido.add_column("cantidad", style="bold")
    table_vencido.add_column("caducidad", style="bold") 
    for i in arr:
        if days_between(str(i['caducidad']))<=0:
            flag=1
            table_vencido.add_row(str(i["item_id"]), i["item_name"], str(i["precio"]), str(i["cantidad"]), str(i["caducidad"]))
    console.print(table_vencido)
            # print(i)
    if flag==0:
        return 0
#Elimina los items que ya están vencidos
def elim_vencidos(arr):
    flag=0
    while(len(arr)>0 and days_between(str(arr[0]['caducidad']))<=0):
        if (elim_item(arr[0]['item_id'], productos) == 1):
            console.print('Item eliminado con exito', style="success")  
            arr.pop(0)
            flag=1
            actualizar()
    if flag==0:
        return 0

#Elimina el primero elemento de la queue
def pop_item(arr):
    if (len(arr)>0 and elim_item(arr[0]['item_id'], productos) == 1):
        console.print('Item eliminado con exito', style="success")
        arr.pop(0)
    else:
        return 0

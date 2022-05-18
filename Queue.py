from LecturaArchivoTexto import  actualizar_pedidos
from rich.console import Console
from rich.theme import Theme
from rich.table import Table

custom_theme = Theme({"success": "green", "error": "bold red"})
console = Console(theme=custom_theme)
#Queue de pedidos
#Mete en la cola un pedido

def enqueue(self, nombre, direccion, numero):
    self.append({'nombre':nombre, 'direccion':direccion,'numero':numero})
    actualizar_pedidos(self)
#Saca de la cola el pedido en la posicion 0
def dequeue(self):
    if(not IsEmpty(self)):
        console.print('Pedido de '+ self[0]['nombre'] + ' ha sido despachado \n', style="success")
        self.pop(0)
        actualizar_pedidos(self)
    else:
        console.print('Todos los pedidos han sido despachados', style="success")
#Revisa si la cola esta vacia
def IsEmpty(self):
    return len(self) == 0
#Vacia la cola de pedidos
def Empty(self):
    while not IsEmpty(self):
            (dequeue(self))
    actualizar_pedidos(self)
#Muestrala cola de pedidos
def ShowQueue(self):
    if not IsEmpty(self):
        for item in self:
            #print('Nombre: ' + item['nombre'] + ' Direccion: ' + item['direccion'] + ' Telefono: '+ str(item['numero']) + '\n')
            table_Q = Table(title="MENU")

            table_Q.add_column("Nombre", style="bold")
            table_Q.add_column("Direccion", style="bold")
            table_Q.add_column("Telefono", style="bold")

            table_Q.add_row(item['nombre'], item['direccion'], str(item['numero']))
            console.print(table_Q)

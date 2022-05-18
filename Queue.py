from LecturaArchivoTexto import  actualizar_pedidos

def enqueue(self, nombre, direccion, numero):
    self.append({'nombre':nombre, 'direccion':direccion,'numero':numero})
    actualizar_pedidos(self)

def dequeue(self):
    if(not IsEmpty(self)):
        print('Pedido de '+ self[0]['nombre'] + ' ha sido despachado \n')
        self.pop(0)
        actualizar_pedidos(self)
    else:
        print('Todos los pedidos han sido despachados')

def IsEmpty(self):
    return len(self) == 0

def Empty(self):
    while not IsEmpty(self):
            (dequeue(self))
    actualizar_pedidos(self)

def ShowQueue(self):
    if not IsEmpty(self):
        for item in self:
            print('Nombre: ' + item['nombre'] + ' Direccion: ' + item['direccion'] + ' Telefono: '+ str(item['numero']) + '\n')

from datetime import datetime
from Encrypting import desencriptar, encriptar
def Leer(self):
    f=open('database.txt','r')
    lines=f.readlines()
    id=0
    nombre=''
    precio=0
    cantidad=0
    cont=0
    caducidad=datetime.today()
    #Lee el archivo de texto linea por linea
    for line in lines:
        #Lee la linea palabra por palabra
        for word in line.split():
            if(cont==0):
                id=int(word)
            if(cont==1):
                nombre=word
            if(cont==2):
                precio=int(word)
            if(cont==3):
                cantidad=int(word)
            if(cont==4):
                caducidad=datetime.strptime(word, '%d-%m-%Y')
            cont+=1
        #agrega a la base de datos
        self.append({'item_id':id, 'item_name':nombre,'precio':precio,'cantidad':cantidad, 'caducidad':caducidad})
        cont=0
    f.close()

def Leer_pedidos(self):
    f=open('pedidos.txt.encrypted','rb')
    lines=f.readlines()
    nombre=''
    direccion=''
    numero=0
    cont=0
    #Lee el archivo de texto linea por linea
    for line in lines:
        #Lee la linea palabra por palabra
        line1=desencriptar(line)
        for word in line1.split():
            if(cont==0):
                nombre=word
            if(cont==1):
                direccion=word
            if(cont==2):
                numero=int(word)
                self.append({'nombre':nombre, 'direccion':direccion,'numero':numero})
                cont=-1
            cont+=1
        #agrega a la base de datos
        
    f.close()

def Leer_clientes(self):
    f=open('clientes.txt.encrypted','rb')
    lines= f.readlines()
    nombre=''
    direccion=''
    numero=0
    tarjeta=0
    cont=0
    #Lee el archivo de texto linea por linea
    for line in lines:
    #Lee la linea palabra por palabra
        line1=desencriptar(line)
        for word in line1.split():
            if(cont==0):
                nombre=word
            if(cont==1):
                direccion=word
            if(cont==2):
                numero=int(word)
            if(cont==3):
                tarjeta=int(word)
                self.append({'nombre':nombre, 'direccion':direccion,'numero':numero, 'tarjeta':tarjeta})
                cont=-1
            cont+=1
        #agrega a la base de datos
        
    f.close()
#Escribe en el archivo de texto la base de datos
def actualizar(self):
    f = open('database.txt', 'w')
    from Quicksort import sort
    sort(self)
    for i in self:
        linea = str(i['item_id'])+ " " +i['item_name']+ " "+ str(i['precio'])+ " " +str(i['cantidad'])+' '+ datetime.strftime(i['caducidad'], '%d-%m-%Y')+"\n"
        f.write(linea)
    f.close()

#Escribe en el archivo encriptado de pedidos
def actualizar_pedidos(self):
    f = open('pedidos.txt.encrypted', 'wb')
    linea=''
    for i in self:
        linea = linea + (i['nombre'])+ " " +i['direccion']+ " "+ str(i['numero']) +"\n"
    f.write(encriptar(linea))
    f.close()

#Escribe en el archivo encriptado de clientes
def actualizar_clientes(self):
    f = open('clientes.txt.encrypted', 'wb')
    linea=''
    for i in self:
        linea =linea+ (i['nombre'])+ " " +i['direccion']+ " "+ str(i['numero'])+ " " + str(i['tarjeta'])+"\n"
    f.write(encriptar(linea))    
    f.close()

from datetime import datetime
from datetime import date
f=open('database.txt','r')
lines=f.readlines()
productos=[]
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
    productos.append({'item_id':id, 'item_name':nombre,'precio':precio,'cantidad':cantidad, 'caducidad':caducidad})
    cont=0
f.close()

#Escribe en el archvito de texto la base de datos
def actualizar():
    f = open('database.txt', 'w')
    for i in productos:
        linea = str(i['item_id'])+ " " +i['item_name']+ " "+ str(i['precio'])+ " " +str(i['cantidad'])+' '+ datetime.strftime(i['caducidad'], '%d-%m-%Y')+"\n"
        f.write(linea)
    f.close()
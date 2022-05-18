# proyecto

El proyecto tiene dos secciones, compras e inventario. 

SEGUNDA ENTREGA: 
Para esta segunda entrega, se convirtió la base de datos a un archivo de texto. Se agregaron fechas de caducidad a los productos, los cuales son ordenados por medio de un heapsort(del más próximo a vencer al menos próximo). También se utilizó un queue para eliminar los productos vencido o próximos a vencer. 

![image](https://user-images.githubusercontent.com/97801260/169165769-eed8642d-0fc7-43e2-b525-95b665a1626c.png)




REQUISITOS:
- Librería Rich ($pip install rich)
- Librería Cryptography ($pip install cryptography)
- Archivo de texto (database.txt)

COMPRAS:
- Agregar productos al carrito
  Input: 
  * Nombre del producto
  Output:
  * Valida que existe la cantidad del producto.
  * Actualiza la base de datos quitando el producto del inventario.
   
- Eliminar productos del carrito
  Input:
  * La posición en que se encuentra el producto en el carrito.
  Output: 
  * Elimina el producto del carrito.
  * Actualiza la base de datos agregando el producto de regreso al inventario.

- Mostrar carrito
  Output:
  * Muestra el contenido del carrito actualizado dentro de una tabla numerada.
 
- Check-Out
  Output:
  * Muestra el carrito.
  * Solicita contestar una pregunta sobre si es cliente antiguo o nuevo.
  * Si es nuevo cliente, le solicita: nombre, direccion, numero de telefono y tarjeta de credito.
  * Si es un cliente antiguo, solo le solicita su numero de telefono para terminar la compra.
  * Muestra el total pagado.
  * Muestra un mensaje confirmando la transacción.

- Salir
  Output:
  * Rergresa al menú principal.


<img width="301" alt="Screen Shot 2022-05-04 at 5 39 07 PM" src="https://user-images.githubusercontent.com/79061296/166842387-431a965e-0aa1-48b9-be6d-12e74437b7d2.png">




INVENTARIO: 
  - Autenticación
    Input:
    * Ususario: admin
    * Contraseña: contrasena 
    Output:
    * Muestra el menú para añadir cantidad, remover cantidad, modificar productos, mostrar productos, añadir item, eliminar item, salir.


  - Añadir Cantidad
    Input:
    * ID
    * Cantidad
    Output: 
    * Actualiza la base de datos.
 
  - Remover Cantidad
    Input:
    * ID
    * Cantidad
    Output:
    * Valida que el producto exista.
    * Valida que haya la suficiente cantidad del producto para descontarlo.
    * Actualiza la base de datos. 
     
  - Modificar Productos
    Este permite hacer tres funciones
    a) Modificar el nombre
      Input: 
      * ID
      * Nuevo nombre
      Output:
      * Actualiza la base de datos.
    b) Modificar el precio
       Input: 
        * ID
        * Nuevo precio
        Output:
        * Actualiza la base de datos.
    c) Modificar la cantidad
       Input: 
      * ID
      * Nueva cantidad
      Output:
      * Actualiza la base de datos.
    d) Modificar fecha de caducidad
       Input: 
      * ID
      * Nueva fecha
      Output:
      * Actualiza la base de datos.
    
  - Mostrar Productos
    Output:
    * Muestra la base de datos de productos actualizada.
    
  - Añadir item
    Input:
    * ID
    * Nombre
    * Precio
    * Cantidad
    Output:
    * Actualiza la base de datos agregando el nuevo item.

  - Eliminar un item
    Input: 
    * ID
    Output: 
    * Actualiza la base datos quitando dicho item.

  - Salir
    Output:
    * Regresa al menú principal.


<img width="295" alt="Screen Shot 2022-05-04 at 5 39 28 PM" src="https://user-images.githubusercontent.com/79061296/166842398-eeee45a3-2005-430b-a856-42327c2d3287.png">

 GESTIONAR PEDIDOS:
 
  - Mostrar pedidos
    * Muestra los pedidos que estan pendientes de ser despachados.
   
  - Despachar pedidos:
    * Despacha el pedido que se realizo primero.


  - Despachar todos los pedidos:
    * Despachar todos los pedidos pendientes.

  
  - Salir:
    * Regresa al menu principal.
  
 ![image](https://user-images.githubusercontent.com/97801260/169166468-c811fa41-a9fa-42e1-bf0f-fdf9787b565e.png)


UNIT TESTING

Funciones

![image](https://user-images.githubusercontent.com/97777878/166841861-af8f0c3a-5fce-4223-9889-160d12614641.png)



Queue

![image](https://user-images.githubusercontent.com/97777878/166842036-a99e5743-0261-44c9-a494-3e5eba621687.png)




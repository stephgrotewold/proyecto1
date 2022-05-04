# proyecto

El proyecto tiene dos secciones, compras e inventario. 

SEGUNDA ENTREGA: 
Para esta segunda entrega, se convirtió la base de datos a un archivo de texto. Se agregaron fechas de caducidad a los productos, los cuales son ordenados por medio de un heapsort(del más próximo a vencer al menos próximo). También se utilizó un queue para eliminar los productos vencido o próximos a vencer. 


REQUISITOS:
- Librería Rich ($pip install rich)
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
  * Muestra el total pagado.
  * Muestra un mensaje confirmando la transacción.

- Salir
  Output:
  * Rergresa al menú principal.



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


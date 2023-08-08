Autor : Gabriel Oliveto

Nombre del Proyecto:
Pagina para uso interno para ventas de autos

Breve descripción o introducción sobre el proyecto.
Este proyecto se realizo para que cualquier salon de ventas de autos pueda realizar las ventas de autos, la aplicacion cuenta con alta, baja, modificacion y borrado de autos, clientes y usuarios. Los datos se persisten en una base de datos Squile3.

1. Para este proyecto se desarrollaron dos App
   -Ventas
   -loguinRegistro

2. Dentro de la App Ventas se desarrollo los siguientes Models
   class Auto
   class Cliente
   class Venta

   Y Se desarrollo las siguientes Views
   class AgregarAutoView
   class BuscarAutoView
   class UpdateAutoView
   class DeleteAutoView
   class AgregarClienteView
   class BuscarClienteView
   class UpdateClienteView
   class DeleteClienteView
   class RealizarVentaView
   class BuscarVentaView
   class UpdateVentaView
   class DeleteVentaView

3. Dentro de la App LoginRegistro se desarrollo los siguientes Models
   class Avatar

   Y Se desarrollo las siguientes Views
   def loguin_request
   def register
   class EditarPerfilView
   class AgregarAvatarView

Tabla de Contenidos

*Inicio
*Caracteristicas
\*Uso

1. Inicio
   .Abrir la carpeta donde se encuentra el proyecto y desde ahi abrir la consola de comandos(CMD).
   .Levantar el servidor usando el comando python manage.py runserver
   .Entrar desde algun navegador de internet a la direccion IP que nos provee el runserver(por default 127.0.0.1:8000) y despues de la direccion IP agragar /ventas

2. Caracteristicas
   .El proyecto cuenta con una pagina de inicio donde el usuario puede registrarse para poder empezar a utilizar la aplicacion.
   .Una ves ingresado al sistema el usuario tiene acceso a cinco secciones ventas, Autos, Clientes, Editar Perfil y agregar Avatar.
   -Dentro de la seccion Ventas se puede realizar la venta del vehiculo previamente teniendo cargado en la base de datos los datos del vehiculo y los datos del cliente, tambien en caso de equivocarse con la venta se puede modificar o eliminar.
   -Dentro de la seccion Autos se puede cargar los datos del vehiculo, marca, modelo y precio, tambien en caso de algun error o no tener mas el modelo cargado para la venta o que haya variado el precio del mismo se puede modificar o eliminar.
   -Dentro de la seccion Cliente se puede cargar los datos del cliente, nombre, apellido y direccion, tambien en caso de algun error de carga de los datos o que el cliente ya no compre mas se puede modificar o eliminar.
   -Dentro de la seccion Editar Perfil, se puede modificar los datos del usuario que utiliza la aplicacion.
   -Dentro de la seccion de Agregar avatar, el usuario puede cargar una foto propia.

3. Uso
   1.En la pagina principal se encuentra los botones de login, registro y administrador, a este ultimo solo el administrador de sitio puede acceder. En caso de tener un usuario y contraseña se podra loguear a la pagina, de no contar con un usuario podra registrarse, el registro le solicitara Usuario, Nombre, Apellido, email y contraseña.
   2.Una ves logueado, dentro de la pagina ya se encuentran cargados datos de autos y clientes, pero si se quiere cargar algun modelo de auto o cliente nuevo, dentro de Autos podra cargar los datos del auto nuevo y dentro de cliente podra cargar los datos de nuevo cliente.
   3.Para realizar una busqueda de una venta, auto o cliente se puede realizar dentro de cada opcion, venta, auto o cliente. En la opcion ventas se encuentra la opcion de buscar venta, la cual se puede buscar por Nombre y Apellido del cliente. En autos aparece el listado de autos, se puede buscar los autos por marca y en clientes aparece un listado con todos los clientes cargados en la base de datos, en la misma se puede buscar un cliente por Nombre, Apellido o Dirección. Tambien dentro de cada opcion, venta, autos y clientes se puede modificar o borrar datos.
   4.Desde la Opcion administracion se puede manejar toda la base de datos, el "usuario" es admin y la "password" es admin123456.
   5.Se creo un usuario de prueba, el "usuario" es Pedro y la "password" es plo123456

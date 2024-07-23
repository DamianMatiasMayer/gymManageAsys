# gymManageSys

Este es un proyecto Django para la gestión de un gimnasio

## Funcionalidades

1. **Herencia de HTML**
   - Todos los templates heredan de `index.html`.

2. **Modelos**
   - Se han definido tres modelos en `models.py`: `Member`, `Trainer`, `Class`.

3. **Formularios de inserción de datos**
   - Se han creado formularios para insertar datos en todas las clases de `models.py`.

4. **Formulario de búsqueda**
   - Se ha implementado un formulario para buscar datos en la base de datos.

## Estructura del proyecto

- `index.html`: Template base para herencia de HTML.
- `contact.html`: Template para el formulario de contacto.
- `models.py`: Definición de los modelos `Member`, `Trainer`, y `Class`.
- `forms.py`: Definición de los formularios `MemberForm`, `TrainerForm`, `ClassForm`, y `SearchForm`.
- `views.py`: Vistas para manejar los formularios y la búsqueda.

## Instrucciones para probar el proyecto

1. Clonar el repositorio.
2. Instalar las dependencias.
3. Ejecutar las migraciones con `python manage.py makemigrations` y `python manage.py migrate`.
4. Iniciar el servidor de desarrollo con `python manage.py runserver`.
5. Navegar a `http://127.0.0.1:8000/` para acceder a la página principal.
6. Probar el formulario de contacto en `http://127.0.0.1:8000/contact/`.
7. Probar el formulario de búsqueda en `http://127.0.0.1:8000/search/`.

## usuario administrador

nombre de usuario = mati
contraseña = damian123

Funcionalidad CRUD para Trainer

Lista de entrenadores
URL: /trainers/

Descripción: Muestra una lista de todos los entrenadores en el sistema. Solo accesible para usuarios logueados.

2. Detalle del entrenador
URL: /trainers/<pk>/

Descripción: Muestra los detalles de un entrenador específico. Reemplaza <pk> con el ID del entrenador. Solo accesible para usuarios logueados.

3. Crear nuevo entrenador
URL: /trainers/new/

Descripción: Permite crear un nuevo entrenador. Solo accesible para usuarios logueados.

4. Editar entrenador
URL: /trainers/<pk>/edit/

Descripción: Permite editar un entrenador existente. Reemplaza <pk> con el ID del entrenador. Solo accesible para usuarios logueados.

5. Eliminar entrenador
URL: /trainers/<pk>/delete/

Descripción: Permite eliminar un entrenador existente. Reemplaza <pk> con el ID del entrenador. Solo accesible para usuarios logueados.

Funcionalidad CRUD para Member

1. Lista de miembros
URL: /members/

Descripción: Muestra una lista de todos los miembros en el sistema. Solo accesible para usuarios logueados.

2. Detalle del miembro
URL: /members/<pk>/

Descripción: Muestra los detalles de un miembro específico. Reemplaza <pk> con el ID del miembro. Solo accesible para usuarios logueados.

3. Crear nuevo miembro
URL: /members/new/

Descripción: Permite crear un nuevo miembro. Solo accesible para usuarios logueados.

4. Editar miembro
URL: /members/<pk>/edit/

Descripción: Permite editar un miembro existente. Reemplaza <pk> con el ID del miembro. Solo accesible para usuarios logueados.

5. Eliminar miembro
URL: /members/<pk>/delete/

Descripción: Permite eliminar un miembro existente. Reemplaza <pk> con el ID del miembro. Solo accesible para usuarios logueados.

Funcionalidad CRUD para Class

1. Lista de clases
URL: /classes/

Descripción: Muestra una lista de todas las clases en el sistema. Solo accesible para usuarios logueados.

2. Detalle de la clase
URL: /classes/<pk>/

Descripción: Muestra los detalles de una clase específica. Reemplaza <pk> con el ID de la clase. Solo accesible para usuarios logueados.

3. Crear nueva clase
URL: /classes/new/

Descripción: Permite crear una nueva clase. Solo accesible para usuarios logueados.

4. Editar clase
URL: /classes/<pk>/edit/

Descripción: Permite editar una clase existente. Reemplaza <pk> con el ID de la clase. Solo accesible para usuarios logueados.

5. Eliminar clase
URL: /classes/<pk>/delete/

Descripción: Permite eliminar una clase existente. Reemplaza <pk> con el ID de la clase. Solo accesible para usuarios logueados.

Pasos para probar la funcionalidad CRUD
Inicia sesión con tu cuenta de superusuario.
Accede a las URLs mencionadas anteriormente para listar, crear, ver detalles, editar y eliminar entrenadores, miembros y clases.
Verifica que las operaciones se realicen correctamente y que solo los usuarios autenticados puedan acceder a estas vistas.
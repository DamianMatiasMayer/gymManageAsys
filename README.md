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


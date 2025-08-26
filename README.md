Movies & Directors (CRUD) - Django + Bootstrap

El proyecto implementa:
1. Script para creación de BD (tablas Directors n Movies).
2. API REST con Django REST Framework.
3. Interfaz en Bootstrap para gestionar directores y películas.

Intalación:
1. Clonar la repo.
2. Crear virtual enviroment
   python -m venv env
   env\Scripts\activate
3. Instalar dependencias:
   pip install -r requirements.txt
4. Generar migraciones y aplicar cambios en la BD:
   python manage.py makemigrations
   python manage.py migrate  
5. Ejecutar el servidor:
   python manage.py runserver

Acceder a la interfaz:
http://localhost:8000/


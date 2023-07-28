pasos: 
Primeramente instalamos la libreria gunicorn, en el entorno con el siguiente comando: "pip install gunicorn"
Nos dirigimos al settings de nuestro proyecto de django remplazamos ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"] y 
agregamos: STATIC_ROOT = os.path.join(BASE_DIR, 'static')
En el archivo urls de nuestro proyecto importamos from django.contrib.staticfiles.urls import staticfiles_urlpatterns y 
agregamos: urlpatterns += staticfiles_urlpatterns()
Luego ponemos el siguiente comando en consola dentro del proyecto "python manage.py collectstatic"
Levantamos el proyecto con gunicor "gunicorn --bind 0.0.0.0:8000 proyectoUno.wsgi"
En una consola hacemos lo siguiente: sudo nano /etc/systemd/system/mi_servicio.service
AL entar dentro colocamos y remplazando con las direcciones que haya creado.

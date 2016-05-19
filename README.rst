laboratoria-mvc
=================

MVC talk for Laboratoria

Comandos:
*************

.. code-block::

	# iniciar la aplicación
	$ python run.py

	# modificar los modelos
	$ sh update_models.sh
	
	# Resetear modelos 
	$ sh create_models.sh


Ejercicios:
*************

Mostrar en las vistas algún elemento que este en el modelo y no se esté mostrando
------------------------------------------------------------------------------------

Debes revisar los modelos y ver si alguna de sus propiedades no se está mostrando en las vistas. De ser así, encuentra el template que las 
está mostrando y edítalo para que muestre ese contenido.


Agregar “logo” al modelo Skill
----------------------------------

1. Ve al modelo Skill y agrega una propiedad **logo**, este deber´a ser de tipo Unicode para rellenar con un link a la imágen. Luego de hacerlo deberás correr el script que resetea la base de datos. 
2. Luego ve al administrador y agrega logo a los skills existentes. 
3. Muestra los logos en alguna vista relevante

Agregar mapa de google a la vista Company
--------------------------------------------------

Puedes hacerlo de cualquier manera, cualquiera estará bien.  


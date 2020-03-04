# populate.py
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mi_sitio_web.settings')

import django
django.setup()

from visitas_granada.models import Visita, Comentario
	
if __name__ == "__main__":
		
	v = Visita(nombre="Alhambra", descripción="Texto Alhambra")
	v.save()

	# ...

	print(Visita.objects.all())

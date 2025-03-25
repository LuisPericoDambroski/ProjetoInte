import os
import projetoint
# projetoint/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projetoint.settings")
application = get_wsgi_application()

app = projetoint  # ⚠️ Nome obrigatório para o Vercel detectar
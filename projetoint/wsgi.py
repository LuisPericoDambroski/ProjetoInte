import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projetoint.settings")
application = get_wsgi_application()

# Fix para o Vercel
app = application
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # 🔥 As URLs do login
    path('', include('t20.urls')),
    path('characters/', include('characters.urls')),  # ✅ já tá certo!
#  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]



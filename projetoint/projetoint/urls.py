from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('characters/', include('characters.urls')),  # 🔥 Certifique-se de que isso está presente!
    path('', include('users.urls')),  # 🔥 As URLs do login
    path('', include('t20.urls'))
]

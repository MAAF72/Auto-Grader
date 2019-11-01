from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls', namespace='apps')),
    path('martor/', include('martor.urls'))
]

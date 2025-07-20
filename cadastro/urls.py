from django.contrib import admin
from django.urls import path, include
from .views import homepage, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('', include('core.urls'))
]

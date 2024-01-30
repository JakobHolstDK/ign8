from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('selinux/', include('selinux.urls')),
]


#SelinuxSerializer
 #   path('', include("main.urls")),
 #   path('selinux/', include('selinux.urls')),
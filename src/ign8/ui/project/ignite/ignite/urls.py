from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("selinux/", include("selinux.urls")),
    path("nudgeme/", include("nudgeme.urls")),
]
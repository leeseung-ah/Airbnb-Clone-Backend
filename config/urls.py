from django.contrib import admin
from django.urls import path, include
from rooms import views


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("rooms/", include("rooms.urls")),
    path("api/v1/users/", include("users.urls")),
]

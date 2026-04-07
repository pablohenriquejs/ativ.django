from django.contrib import admin
from django.urls import path
from core.views import lista, criar, editar, deletar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista),
    path('criar/', criar),
    path('editar/<int:id>/', editar),
    path('deletar/<int:id>/', deletar),
]
from django.urls import path
from . import views, forms

urlpatterns = [
    path(r'', views.main_page, name='main_page'),
]
from django.urls import path
from .views import index, lead_detail, lead_create


app_name = 'leads'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', lead_detail, ),
    path('create/', lead_create, ),
]

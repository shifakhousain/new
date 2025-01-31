from . import views 
from django.urls import path

app_name = 'food'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),  # Corrected line
    path('item/', views.item, name='item'),
]

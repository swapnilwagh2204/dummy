from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]

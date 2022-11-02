from django.urls import path
from todoapp import views


urlpatterns = [

    path('show/', views.show),
    path('delete/<int:tid>',views.delete),
    path('update/<int:tid>',views.update)
]

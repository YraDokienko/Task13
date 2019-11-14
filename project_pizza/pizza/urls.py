from django.urls import path
from . import views


urlpatterns = [
    path('', views.PizzaView.as_view()),
    path('pizzaform/', views.PizzaFormView.as_view()),
    path('pizzaform/<int:pk>/edit/', views.PizzaUpdateView.as_view()),
]

from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.PersonList.as_view(), name='person-list'),
    path('persons/<int:pk>/', views.PersonDetail.as_view(), name='person-detail'),
]

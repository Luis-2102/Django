from django.urls import path
from . import views
from .views import RentListView, RentDetailView, RentCreate, RentUpdateView, RentDeleteView

rent_patterns = ([
    path('', RentListView.as_view(), name='rents'),
    path('<int:pk>/<slug:slug>/', RentDetailView.as_view(), name='rent'),
    path('create/', RentCreate.as_view(), name='rent_create'),
    path('update/<int:pk>/', RentUpdateView.as_view(), name='rent_update'),
    path('delete/<int:pk>/', RentDeleteView.as_view(), name='rent_delete'),
], 'rents')
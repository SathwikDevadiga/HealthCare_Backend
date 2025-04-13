from django.urls import path
from .views import *

urlpatterns = [
    path('', PatientListCreateView.as_view(), name='patient-list'),
    
    path('<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
]

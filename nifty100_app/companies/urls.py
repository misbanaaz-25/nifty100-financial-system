from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/companies', views.CompanyViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('companies/', views.companies_list, name='companies'),
    path('api/data/', views.api_companies, name='api_companies'),
    path('', include(router.urls)),
]
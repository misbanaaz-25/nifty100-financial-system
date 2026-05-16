from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Company
from .serializers import CompanySerializer
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "postgresql://postgres:admin123@localhost:5432/nifty100_dw"
)

def home(request):
    return render(request, 'home.html')

def companies_list(request):
    df = pd.read_sql("SELECT * FROM companies", engine)
    companies = df.to_dict('records')
    return JsonResponse({'companies': companies})

@api_view(['GET'])
def api_companies(request):
    df = pd.read_sql("SELECT * FROM companies", engine)
    df = df.fillna('')
    companies = df.to_dict('records')
    return Response(companies)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_id, name='report_id'),
    path('success/', views.success, name='success'),
    path('search/', views.search_id, name='search_id'),
    path('', views.landing_page, name='landing')
]
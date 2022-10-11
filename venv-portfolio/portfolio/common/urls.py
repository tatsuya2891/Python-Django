from django.urls import path
from . import views


app_name = 'common'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('works/', views.WorksView.as_view(), name='works'),
]
from django.urls import path
from . import views

app_name = 'inquiry'
urlpatterns = [
    path('', views.InquiryView.as_view(), name="inquiry"),
]
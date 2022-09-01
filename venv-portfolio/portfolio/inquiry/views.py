from django.shortcuts import render
from django.views import generic
from .forms import InquiryForm

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm


    #ポートフォリオから「コンタクト」削除するため、inquiryアプリは削除する
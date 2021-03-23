from django.shortcuts import render
from django.views.generic import ListView, FormView
from .forms import *
from .models import Blog


class ViewValidation(FormView):
    model = Blog
    form_class = ValidForm
    template_name = 'custom_admin/validation.html'
    success_url = '/'


class ViewForJquery(FormView):
    model = Blog
    form_class = ValidForm
    template_name = 'custom_admin/for_jquery.html'
    success_url = '/'

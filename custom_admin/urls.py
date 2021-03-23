from django.urls import path
from .views import *

urlpatterns = [
    path('', ViewValidation.as_view()),
    path('jquery/', ViewForJquery.as_view(), name='jquery')
]

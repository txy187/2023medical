from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('section<int:num>/', TemplateView.as_view(template_name='index.html'), name='section'),
]
from django.urls import path
from django.views.generic import TemplateView

app_name='yfcase'
urlpatterns = [
  path('', TemplateView.as_view(template_name='base.html'))
]

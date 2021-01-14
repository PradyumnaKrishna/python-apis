from django.conf.urls import url
from .views import plotView

urlpatterns = [
    url(r'^$', plotView.as_view(), name='plot'),
]

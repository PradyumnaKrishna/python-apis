from django.conf.urls import url
from .views import itemsView

urlpatterns = [
    url(r'^$', itemsView.as_view(), name='items'),
]

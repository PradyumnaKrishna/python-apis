from django.conf.urls import url
from .views import bookingView, cancelView

urlpatterns = [
    url(r'booking', bookingView.as_view(), name='booking'),
    url(r'cancel', cancelView.as_view(), name='cancel'),
]

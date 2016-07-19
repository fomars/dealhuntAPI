from collector import views
from django.conf.urls import url

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^savetask', views.savetask, name='savetask')
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',  views.home, name='index'),
    url(r'^form/',views.form, name="form"),
    url(r'^table/',views.table,name='table'),
    url(r'^forminsert/',views.forminsert,name="forminsert")
]
from django.views.generic import ListView
from base.models import Articles
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^goods/$', views.goods, name='goods'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^$', ListView.as_view(queryset=Articles.objects.all()[:20],
                                template_name="html/index.html"))
]

from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.index,name ='home'),
    url(r'^profile/',views.profile,name= 'profile'),
    url(r'^business/',views.create_business,name='create_business'),
    url(r'^new/post$', views.new_post, name='newpost'),
    url(r'^search/$', views.search, name='search'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
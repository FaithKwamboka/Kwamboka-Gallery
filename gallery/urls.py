from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='home'),
    path('search', views.search_results, name='search_results'),
    path('image',views.get_image_by_id,name ='image'),
    # path('location/<id>',views.filter_by_location,name='location')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
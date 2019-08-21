from django.urls import path

from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('mandatory_playlist', views.mandatory_playlist, name='mandatory_playlist'),
    path('voluntary_playlist', views.voluntary_playlist, name='voluntary_playlist'),
    path('view/<str:video>', views.video_view, name='video_view')
]

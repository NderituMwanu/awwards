from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
# from django.contrib.auth import views


urlpatterns = [
    path('', views.PostList, name='home'),
    path('post-project/',views.PostNew,name="post-project"),
    path('profile/',views.profile,name="profile"),
    path('logout/',views.logout_view,name="logout"),

    path('accounts/', include('registration.backends.simple.urls')),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
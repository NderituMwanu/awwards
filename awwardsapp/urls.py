from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
# from django.contrib.auth import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^logout/$', auth_views.LogoutView, {"next_page": '/'})
    url(r'^logout/$', views.logout, {"next_page": '/accounts/login'}), 
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
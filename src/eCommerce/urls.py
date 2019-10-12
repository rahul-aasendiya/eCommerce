"""eCommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf.urls.static import static 
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from account import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^comments/', include("comments.urls")),
    url(r'^login/$',views.login_view,name='login'),
    url(r'^accounts/login/$',views.login_view,name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^singup/$',views.login_view,name='singup'),
    # url(r'^singup/',views.register_view,name='singup'),
    url(r'^custmize/$',views.edit_all,name='custmize'),
    url(r'^', include("blog.urls")),
    url(r'^api/Post/', include("api.urls")),
    # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
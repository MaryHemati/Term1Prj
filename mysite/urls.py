"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello),
    path('upload/',views.upload,name='upload'),
    path('blackwhite/',views.blackwhite,name='blackwhite'),
    path('rotate/',views.rotate,name='rotate'),
    path('Display/',views.Display, name='Display'),
    path('resize/',views.resize,name='resize'),
    path('crop/',views.crop,name='crop'),
    path('shared/',views.shared,name='shared'),
    path('show_shared_photos',views.show_shared_photos,name='show_shared_photos'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns +static(settings.SHARED_URL, document_root=settings.SHARED_ROOT)

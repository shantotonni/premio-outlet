"""premio URL Configuration

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
from django.conf.urls import url, include
from premioapp.views import redirect_url,market_update,send_test_notification

admin.site.site_header = "Premio Outlet Admin"
admin.site.site_title = "Premio Outlet Admin"
admin.site.index_title = "Premio Outlet"

urlpatterns = [
    path('', redirect_url, name="redirect-url"),
    path('premio-outlet/', admin.site.urls),
    path('premio-outlet/', include('premioapp.urls')),
    path('premio-outlet/send-test-notification-fpm',send_test_notification),
]

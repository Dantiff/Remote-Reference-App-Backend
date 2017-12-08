"""project URL Configuration

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
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from core.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api/users/register/$', UserCreate.as_view(), name='user-create'),
    url(r'^api/customers/(?P<username>[^/]+)/(?P<phone>[^/]+)/$', CustomerDetails.as_view(), name='customer-details'),
    url(r'^api/customers/fetch_debtors/$', DebtorsDetails.as_view(), name='debtors-details'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('core.urls')),
    url(r'^due_listing/create/$', CreateDueListing, name='create-due-listing'),
]

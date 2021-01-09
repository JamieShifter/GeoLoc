"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

import new_api.views as views
import new_api.api_views as api_views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('redirect/', views.redirect_view),
    path('get/<str:ip_address>/', views.get_local),
    path('get/', views.get_local),
    path('api/v1/geoloc/', api_views.Ip_GeoLocation.as_view()),
    path('api/v1/geoloc/new', api_views.GeolocationCreate.as_view()),
    path('api/v1/geoloc/<int:id>/', api_views.GeolocationRetrieveUpdateDestroy.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.home, name='home'),
]

handler404 = 'new_api.views.error_404'
handler500 = 'new_api.views.error_500'
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from premioapp.api import api_views
from premioapp.api import auth_views

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Premio Outlet API')

urlpatterns = [
    
    
    path('api/login/',views.obtain_auth_token,name='api-auth-token-login'),
    path('api/logout/', api_views.Logout.as_view(), name='api-auth-token-logout'),
    url('api-documentation/', schema_view),
    path('api/change-password/',auth_views.ChangePasswordView.as_view(),name='change-password'),
    
    path('api/authenticated-user-info/', api_views.authenticated_user_info,name='auth-user-info'),
    path('api/user/', api_views.UserList.as_view()),
    path('api/user/<int:pk>/', api_views.UserDetail.as_view()), 
    
    path('api/base/', api_views.BaseList.as_view()),
    path('api/route/', api_views.RouteList.as_view()),
    path('api/route-day/', api_views.RouteDayList.as_view()),
    path('api/category/', api_views.CategoryList.as_view()),
    path('api/category/<int:pk>/',api_views.CategoryDetail.as_view()),
    path('api/outlet-type/', api_views.OutletTypeList.as_view()),
    path('api/outlet-type/<int:pk>/',api_views.OutletTypeDetail.as_view()),
    
    path('api/market/', api_views.MarketList.as_view()),
    path('api/market-with-parent/',api_views.MarketListWithParent.as_view()),
    #path('user/<str:username>/market', api_views.get_markets_of_user,name='user-markets'),
    path('api/market/<int:pk>/',api_views.MarketDetail.as_view()),
    path('api/outlet-type/', api_views.OutletTypeList.as_view()),
    path('api/outlet/', api_views.OutletList.as_view()),
    path('api/outlet/<int:pk>/',api_views.OutletDetail.as_view()),
    #path('user/<str:username>/outlet', api_views.UserOutletList().as_view(),name='user-outlets'),
    
    path('api/apk-version/<int:pk>/',api_views.ApkVersionDetail.as_view()),
    path('api/live-location/',api_views.LiveLocationDetail.as_view()),
]

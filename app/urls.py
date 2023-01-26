from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView,LoginAPI,getUser
from knox import views as knox_views


app_name = "app"
urlpatterns = [
  path("get-details/",UserDetailAPI.as_view(),name="get-details"),
  path('register/',RegisterUserAPIView.as_view(),name="register"),
   path('login/', LoginAPI.as_view(), name='login'),
  path('logout/', knox_views.LogoutView.as_view(), name='logout'),
  path("users/<str:pk>/",getUser,name="getNote")
]
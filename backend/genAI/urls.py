from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('notes/', views.getNotes, name='users'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', views.getUserDetails, name='user_details'), 
    # path('test-post/', views.test_post, name='test_post'),
    path('register/',views.create,name="create"),
    path('generate-content/',views.generate_content,name="generate_content"),
    path('generate-voice/',views.generate_voice,name="generate_voice"),
    # path('generate-image/', views.generate_image, name='generate_image'),
    path('update-ngrok-url/',views.update_ngrok_url,name='update_ngrok_url')
]


# from rest_framework_simplejwt.views import (
#     TokenRefreshView,
# )


# urlpatterns = [
#     path("", views.get_routes, name="get_routes"),
#     path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path("list/", views.getUSERS, name="get_users"),
# ]
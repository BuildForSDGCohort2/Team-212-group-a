from django.urls import path, include
from .authApi import RegistrationAPI, UserAPI, LoginAPI, ProfileAPI, updateProfile
from knox import views as knox_views

urlpatterns=[
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegistrationAPI.as_view(),name='register'),
    path('api/auth/login', LoginAPI.as_view(), name='login'),
    path('api/auth/user', UserAPI.as_view(), name='user'),
    path('api/auth/profile', ProfileAPI.as_view(), name='profile'),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='logout'),
    path('api/auth/logout', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/auth/profile/update', updateProfile,name="profileUpdate"),
]
from django.urls import path , include
from .views import CustomLoginView , CustomRegisterView , activate_account
app_name = 'users'

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('register',CustomRegisterView.as_view(),name='register'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('activate/<uidb64>/<token>/', activate_account, name='activate'),
]
from django.urls import path
from .views import SignupPageView, profile, account, account_search
urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('update/', profile, name='profile1'),
    path('<user_id>/', account, name='account'),
    path('', account_search, name='search'),
]
from django.urls import path

from .views import friends, profile, requests, sendFriendReq


urlpatterns = [
    path("friends/", friends, name="friends"),
    path("friends/profile", profile, name="profile"),
    path("friends/requests/", requests, name="requests"),  
    path("friend_request/", sendFriendReq, name="friend_request"),
]

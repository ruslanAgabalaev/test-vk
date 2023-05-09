from django.urls import path
from . import views
app_name = 'my_friends'
urlpatterns = [
    path('friends/', views.FriendsView.as_view(), name='friends'),
    path('friends/<int:pk>/', views.FriendsDetailView.as_view(), name='friend_detail'),
    path('groups/', views.GroupsView.as_view(), name='groups'),
]

from django.urls import path
from .views import user_view

urlpatterns = [
    path('register/', user_view.RegisterUserView.as_view()),
    path('users/', user_view.UserListView.as_view()),
    path('user/', user_view.UserView.as_view()),
    path('user/leagues/', user_view.UserLeagues.as_view())
]
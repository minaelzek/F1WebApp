from django.urls import path
from .views import user_view

urlpatterns = [
    path('users/', user_view.F1UserListView.as_view())
]
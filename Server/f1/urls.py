from django.urls import path
from .views import user_view, login_view, fantasy_view
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # DOCS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # User APIS
    path('user/<int:user_id>', user_view.UserView.as_view()),
    path('register/user/', login_view.RegisterUserView.as_view()),
    path('login/user/', login_view.LoginUserView.as_view()),
    path('logout/user/', login_view.LogoutUserView.as_view()),
    path('user/<int:user_id>/leagues/', user_view.UserLeagues.as_view()),
    path('user/<int:user_id>/league/', user_view.UserCreateLeague.as_view()),
    path('user/<int:user_id>/league/<int:league_id>', user_view.UserLeague.as_view()),
    # Fantasy APIs
    path('user/<int:user_id>/league/<int:league_id>/constructorPrediction/<int:prediction_id>', fantasy_view.ConstructorPredictionView.as_view())
]
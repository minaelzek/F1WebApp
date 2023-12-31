from django.urls import path
from .views import user_view, login_view, fantasy_view
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # DOCS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # User APIS
    path('user/', user_view.UserView.as_view()),
    path('register/user/', login_view.RegisterUserView.as_view()),
    path('login/user/', login_view.LoginUserView.as_view()),
    path('logout/user/', login_view.LogoutUserView.as_view()),
    path('user/leagues/', user_view.UserLeagues.as_view()),
    path('user/league/', user_view.UserCreateLeague.as_view()),
    path('user/league/<int:league_id>', user_view.UserLeague.as_view()),
    # Fantasy APIs
    path('user/league/<int:league_id>/constructorPrediction', fantasy_view.ConstructorPredictionCreateView.as_view()),
    path('user/league/<int:league_id>/constructorPrediction/<int:prediction_id>', fantasy_view.ConstructorPredictionView.as_view()),
    path('user/league/<int:league_id>/weekend_prediction', fantasy_view.WeekendEventPredictionCreateView.as_view()),
    path('user/league/<int:league_id>/weekend_prediction/<int:prediction_id>', fantasy_view.WeekendEventPredictionView.as_view()),
]
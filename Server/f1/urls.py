from django.urls import path
from .views import user_view
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # DOCS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # APIS
    path('user/', user_view.UserView.as_view()),
    path('user/register/', user_view.RegisterUserView.as_view()),
    path('user/leagues/', user_view.UserLeagues.as_view())
]
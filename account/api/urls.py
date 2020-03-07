from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from account.api.views import(UserViewSet,
                              ProfileViewSet,
                              ProfileUpdateAPIView,
                              ProfileDetailsAPIView,
                              # ObtainAuthTokenView,
UserPartialUpdateView,
                              login)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
# router.register(r'profile', ProfileViewSet, basename='profile')
urlpatterns = [

    path('', include(router.urls)),
    path('profile/', ProfileViewSet.as_view(), name="profile"),
    path('profile/<int:id>/', ProfileDetailsAPIView.as_view(), name="profile-view"),
    path('login/', login, name="login"),
    path('user-profile/<int:id>/edit/', ProfileUpdateAPIView.as_view(), name="profile-update"),
    path('profile/<int:id>/edit/', UserPartialUpdateView.as_view(), name="profile-update"),

    # path('profile/<int:user_id>/', include(router.urls))

]

urlpatterns += router.urls

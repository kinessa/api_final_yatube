from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register(r'follow', FollowViewSet, basename='follows')

urlpatterns_jwt = [
    path('create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='jwt_verify')]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/jwt/', include(urlpatterns_jwt)),
]

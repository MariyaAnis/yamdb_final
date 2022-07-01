from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoriesViewSet, CommentViewSet, GenresViewSet,
                    ReviewViewSet, TitlesViewSet, UserViewSet, get_jwt_token,
                    register)

app_name = 'api'
router_v1 = DefaultRouter()

router_v1.register(r'users', UserViewSet)
router_v1.register(r'genres', GenresViewSet, basename='genres')
router_v1.register(r'categories', CategoriesViewSet, basename='categories')
router_v1.register(r'titles', TitlesViewSet, basename='titles')
router_v1.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewViewSet, basename='reviews')
router_v1.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
                   r'/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token')
]

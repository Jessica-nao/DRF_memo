# posts/urls.py
from django.urls import path
from rest_framework.routers import SimpleRouter

# from .views import PostList, PostDetail, UserDetail, UserList

from .views import UserViewset, PostViewSet


router = SimpleRouter()
router.register('users', UserViewset, basename='users')
router.register('',PostViewSet, basename='posts')

urlpatterns = router.urls

# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),    
# ]
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import FragmentsList, FragmentsTestViewSet, FragmentsViewSet


router = SimpleRouter()
router.register('', FragmentsViewSet, basename='fragments')


urlpatterns = [
    path('list/', FragmentsList.as_view(), name='list'),
]
urlpatterns += router.urls

# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),    
# ]
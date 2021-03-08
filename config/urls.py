from django.contrib import admin
from django.urls import path, include # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')), # 追加
    # path('api/', include('api.urls')), # 追加
    # path('api/', include('todos.urls')),
    path('api/v1/posts/', include('posts.urls')),
    path('api/v1/fragments/', include('fragments.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
]
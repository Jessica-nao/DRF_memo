from django.contrib.auth import get_user_model
from django.db.models import query
from rest_framework import generics, permissions,viewsets, generics
from django_filters import rest_framework as filters
from posts.views import UserSerializer


from .models import Fragment
from .serializers import FragmentSerializer

class FragmentsFilter(filters.FilterSet):
    start = filters.DateTimeFromToRangeFilter()
    member = filters.ModelChoiceFilter(queryset=get_user_model().objects.all())
    
    class Meta:
        model = Fragment
        fields = ['start','member',]


class FragmentsViewSet(viewsets.ModelViewSet):
    queryset = Fragment.objects.all()
    serializer_class = FragmentSerializer
    # filter_fields = ('__all__')
    filter_class = FragmentsFilter


class FragmentsList(generics.ListAPIView):
    serializer_class = FragmentSerializer

    def get_queryset(self):
        user = self.request.user
        return Fragment.objects.filter(member=user)
    


class FragmentsTestViewSet(viewsets.ModelViewSet):
    serializer_class = FragmentSerializer
    queryset = Fragment.objects.all()




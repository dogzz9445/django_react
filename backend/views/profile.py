from rest_framework import generics, serializers
from rest_framework.response import Response

from backend.models.profile import Profile

class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'created_date')

# Create your views here.
class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)

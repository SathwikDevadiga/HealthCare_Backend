from rest_framework import generics, permissions
from .models import Mapping
from .serializers import MappingSerializer

class MappingListCreateView(generics.ListCreateAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Mapping.objects.filter()

    def perform_create(self, serializer):
        serializer.save()

class MappingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]




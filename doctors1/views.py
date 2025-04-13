from rest_framework import generics, permissions
from .models import Doctor1
from .serializers import DocatorSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    serializer_class = DocatorSerializer

    def get_permissions(self):
        if self.request.method == 'POST':  # Authentication required for POST (Create)
            return [permissions.IsAuthenticated()]
        return []  # No authentication required for GET (List)

    def get_queryset(self):
        return Doctor1.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor1.objects.all()
    serializer_class = DocatorSerializer
    



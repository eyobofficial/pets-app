from rest_framework import viewsets
from .models import Pet
from .serializers import PetSerializer


class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer

    def get_queryset(self):
        return Pet.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

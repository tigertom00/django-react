from leads import models
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = models.Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer

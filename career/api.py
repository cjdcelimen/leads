from career.models import Leads
from rest_framework import viewsets, permissions
from .serializers import LeadsSerializer

# lead viewset
class LeadsViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadsSerializer

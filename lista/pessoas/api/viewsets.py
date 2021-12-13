from rest_framework import viewsets
from pessoas.api import serializers
from pessoas import models

class PessoasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PessoasSerializer
    queryset = models.Pessoas.objects.all()
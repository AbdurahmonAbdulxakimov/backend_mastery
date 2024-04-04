from rest_framework.generics import ListAPIView

from estate import models, serializers


class EstateListAPIView(ListAPIView):
    queryset = models.Estate.objects.all()
    serializer_class = serializers.EstateSerializer

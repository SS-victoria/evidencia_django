from rest_framework.viewsets import ModelViewSet
from apps.movimientoparte.api.serializers import MovimientoParteSerializer,MovimientoRegistersSerializers
from apps.movimientoparte.models import MovimientoParte


class MovimientoParteViewSet(ModelViewSet):
    serializer_class = MovimientoParteSerializer
    queryset = MovimientoParte.objects.all()
    http_method_names=['get','delete']
    
class MovimientoRegisters(ModelViewSet):
    serializer_class=MovimientoRegistersSerializers
    queryset = MovimientoParte.objects.all()
    http_method_names=['post','put']

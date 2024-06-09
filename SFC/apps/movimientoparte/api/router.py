from rest_framework.routers import DefaultRouter
from apps.movimientoparte.api.views import MovimientoParteViewSet,MovimientoRegisters

router_movimientoParte = DefaultRouter()
router_movimientoParte.register(prefix="movimientoParte", basename="MovimientoParte", viewset=MovimientoParteViewSet)
router_movimientoParte.register(prefix="movimientoRegister", basename="movimientoRegister", viewset=MovimientoRegisters)

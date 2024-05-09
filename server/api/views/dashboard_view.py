from ninja import Router
from ninja.responses import Response

from django.http.request import HttpRequest

from api.repositories.farm_rural_producer_repository import (
    FarmRuralProducerRepository,
)
from api.repositories.farm_rural_culture_producer_repository import (
    FarmCultureRuralProducerRepository,
)

from api.services.dashboard_data_calculator import DashboardDataCalculatorService
from api.schemas.dashboard_schemas import DashboardDataSchema


router = Router(tags=["Dashboard"])

__farm_rural_producer_repository = FarmRuralProducerRepository()
__farm_culture_rural_producer_repository = FarmCultureRuralProducerRepository()


@router.get("", summary="Data for dashboards", response=DashboardDataSchema)
def get_dashboard_data(request: HttpRequest):
    service = DashboardDataCalculatorService(
        farm_rural_producer_repository=__farm_rural_producer_repository,
        farm_culture_rural_producer_repository=__farm_culture_rural_producer_repository,
    )
    dashboard_data = service.execute()

    return Response(dashboard_data)

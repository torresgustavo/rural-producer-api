from uuid import UUID

from api.repositories.rural_producer_repository import RuralProducerRepository


class RemoveRuralProducerService:

    def __init__(
        self,
        rural_producer_repository: RuralProducerRepository,
    ) -> None:
        self.__rural_producer_repository = rural_producer_repository

    def execute(self, _id: UUID):
        rural_producer = self.__rural_producer_repository.get_by_id(id=_id)
        self.__rural_producer_repository.remove(rural_producer)

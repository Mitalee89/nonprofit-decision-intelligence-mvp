from typing import Optional

from app.models.grant import Grant
from app.repositories.grant_repository import GrantRepository
from app.schemas.grant import GrantCreate, GrantUpdate


class GrantService:

    def __init__(
        self,
        grant_repository: GrantRepository,
    ):
        self.grant_repository = grant_repository

    def create_grant(
        self,
        request: GrantCreate,
    ) -> Grant:

        grant = Grant(**request.model_dump())

        return self.grant_repository.create(grant)

    def get_grant(
        self,
        grant_id: int,
    ) -> Optional[Grant]:

        return self.grant_repository.get_by_id(grant_id)

    def get_all_grants(
        self,
    ) -> list[Grant]:

        return self.grant_repository.get_all()

    def update_grant(
        self,
        grant_id: int,
        request: GrantUpdate,
    ) -> Optional[Grant]:

        grant = self.grant_repository.get_by_id(grant_id)

        if grant is None:
            return None

        updates = request.model_dump(exclude_unset=True)

        for field, value in updates.items():
            setattr(grant, field, value)

        return self.grant_repository.update(grant)

    def delete_grant(
        self,
        grant_id: int,
    ) -> bool:

        return self.grant_repository.delete(grant_id)

    def get_open_grants(
        self,
    ) -> list[Grant]:

        return self.grant_repository.get_open_grants()
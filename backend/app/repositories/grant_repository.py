from sqlmodel import Session

from app.models.grant import Grant
from app.repositories.base_repository import BaseRepository


class GrantRepository(BaseRepository[Grant]):

    def __init__(self, session: Session):
        super().__init__(Grant, session)
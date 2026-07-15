from sqlmodel import Session, select

from app.models.enums import GrantStatus
from app.models.grant import Grant
from app.repositories.base_repository import BaseRepository


class GrantRepository(BaseRepository[Grant]):

    def __init__(self, session: Session):
        super().__init__(Grant, session)

    def get_open_grants(self) -> list[Grant]:
        statement = select(Grant).where(
            Grant.status == GrantStatus.OPEN
        )
        return list(self.session.exec(statement))
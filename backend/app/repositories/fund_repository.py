from sqlmodel import Session

from app.models.fund import Fund
from app.repositories.base_repository import BaseRepository


class FundRepository(BaseRepository[Fund]):

    def __init__(self, session: Session):
        super().__init__(Fund, session)
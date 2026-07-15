from sqlmodel import Session, select

from app.models.enums import FundStatus
from app.models.fund import Fund
from app.repositories.base_repository import BaseRepository


class FundRepository(BaseRepository[Fund]):

    def __init__(self, session: Session):
        super().__init__(Fund, session)

    def get_open_funds(self) -> list[Fund]:
        statement = select(Fund).where(
            Fund.status == FundStatus.OPEN
        )
        return list(self.session.exec(statement))

    def get_by_campaign(self, campaign_id: int) -> list[Fund]:
        statement = select(Fund).where(
            Fund.campaign_id == campaign_id
        )
        return list(self.session.exec(statement))
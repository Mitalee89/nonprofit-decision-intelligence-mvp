from sqlmodel import Session, select

from app.models.campaign import Campaign
from app.models.enums import CampaignStatus
from app.repositories.base_repository import BaseRepository


class CampaignRepository(BaseRepository[Campaign]):

    def __init__(self, session: Session):
        super().__init__(Campaign, session)

    def get_active_campaigns(self) -> list[Campaign]:
        statement = select(Campaign).where(
            Campaign.status == CampaignStatus.ACTIVE
        )
        return list(self.session.exec(statement))
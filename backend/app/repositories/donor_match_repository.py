from sqlmodel import Session, select

from app.models.donor_match import DonorMatch
from app.repositories.base_repository import BaseRepository


class DonorMatchRepository(BaseRepository[DonorMatch]):

    def __init__(self, session: Session):
        super().__init__(DonorMatch, session)

    def get_by_campaign(
        self,
        campaign_id: int,
    ) -> list[DonorMatch]:

        statement = select(DonorMatch).where(
            DonorMatch.campaign_id == campaign_id
        )

        return list(
            self.session.exec(statement)
        )

    def delete_by_campaign(
        self,
        campaign_id: int,
    ) -> None:

        matches = self.get_by_campaign(
            campaign_id
        )

        for match in matches:
            self.session.delete(match)

        self.session.commit()
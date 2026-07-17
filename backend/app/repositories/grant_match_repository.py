from sqlmodel import Session, select

from app.models.grant_match import GrantMatch
from app.repositories.base_repository import BaseRepository


class GrantMatchRepository(BaseRepository[GrantMatch]):

    def __init__(self, session: Session):
        super().__init__(GrantMatch, session)

    def get_by_campaign(
        self,
        campaign_id: int,
    ) -> list[GrantMatch]:

        statement = select(GrantMatch).where(
            GrantMatch.campaign_id == campaign_id
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
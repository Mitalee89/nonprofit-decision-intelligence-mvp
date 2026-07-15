from sqlmodel import Session, select

from app.models.donation import Donation
from app.repositories.base_repository import BaseRepository


class DonationRepository(BaseRepository[Donation]):

    def __init__(self, session: Session):
        super().__init__(Donation, session)

    def get_by_donor(self, donor_id: int) -> list[Donation]:
        statement = select(Donation).where(
            Donation.donor_id == donor_id
        )
        return list(self.session.exec(statement))

    def get_by_fund(self, fund_id: int) -> list[Donation]:
        statement = select(Donation).where(
            Donation.fund_id == fund_id
        )
        return list(self.session.exec(statement))
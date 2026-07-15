from sqlmodel import Session, select

from app.models.donor import Donor
from app.repositories.base_repository import BaseRepository


class DonorRepository(BaseRepository[Donor]):

    def __init__(self, session: Session):
        super().__init__(Donor, session)

    def get_by_email(self, email: str) -> Donor | None:
        statement = select(Donor).where(
            Donor.email == email
        )
        return self.session.exec(statement).first()

    def get_active_donors(self) -> list[Donor]:
        statement = select(Donor).where(
            Donor.is_active == True
        )
        return list(self.session.exec(statement))
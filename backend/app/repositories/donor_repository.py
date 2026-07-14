from sqlmodel import Session

from app.models.donor import Donor
from app.repositories.base_repository import BaseRepository


class DonorRepository(BaseRepository[Donor]):

    def __init__(self, session: Session):
        super().__init__(Donor, session)
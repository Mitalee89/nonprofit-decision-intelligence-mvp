from typing import Optional

from app.models.donor import Donor
from app.repositories.donor_repository import DonorRepository
from app.schemas.donor import DonorCreate, DonorUpdate


class DonorService:

    def __init__(
        self,
        donor_repository: DonorRepository,
    ):
        self.donor_repository = donor_repository

    def create_donor(
        self,
        request: DonorCreate,
    ) -> Donor:

        existing = self.donor_repository.get_by_email(
            request.email
        )

        if existing:
            raise ValueError(
                "Donor with this email already exists."
            )

        donor = Donor(**request.model_dump())

        return self.donor_repository.create(donor)

    def get_donor(
        self,
        donor_id: int,
    ) -> Optional[Donor]:

        return self.donor_repository.get_by_id(donor_id)

    def get_all_donors(
        self,
    ) -> list[Donor]:

        return self.donor_repository.get_all()

    def update_donor(
        self,
        donor_id: int,
        request: DonorUpdate,
    ) -> Optional[Donor]:

        donor = self.donor_repository.get_by_id(donor_id)

        if donor is None:
            return None

        updates = request.model_dump(exclude_unset=True)

        for field, value in updates.items():
            setattr(donor, field, value)

        return self.donor_repository.update(donor)

    def delete_donor(
        self,
        donor_id: int,
    ) -> bool:

        return self.donor_repository.delete(donor_id)

    def get_active_donors(
        self,
    ) -> list[Donor]:

        return self.donor_repository.get_active_donors()
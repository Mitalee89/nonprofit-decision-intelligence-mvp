from typing import Optional

from app.models.donation import Donation
from app.repositories.campaign_repository import CampaignRepository
from app.repositories.donation_repository import DonationRepository
from app.repositories.donor_repository import DonorRepository
from app.repositories.fund_repository import FundRepository
from app.schemas.donation import DonationCreate, DonationUpdate


class DonationService:

    def __init__(
        self,
        donation_repository: DonationRepository,
        donor_repository: DonorRepository,
        fund_repository: FundRepository,
        campaign_repository: CampaignRepository,
    ):
        self.donation_repository = donation_repository
        self.donor_repository = donor_repository
        self.fund_repository = fund_repository
        self.campaign_repository = campaign_repository

    def create_donation(
        self,
        request: DonationCreate,
    ) -> Donation:

        donor = self.donor_repository.get_by_id(request.donor_id)

        if donor is None:
            raise ValueError("Donor not found.")

        fund = self.fund_repository.get_by_id(request.fund_id)

        if fund is None:
            raise ValueError("Fund not found.")

        donation = Donation(**request.model_dump())

        donation = self.donation_repository.create(donation)

        # Update Fund
        fund.balance += donation.amount
        fund.total_received += donation.amount

        self.fund_repository.update(fund)

        # Update Campaign
        campaign = self.campaign_repository.get_by_id(
            fund.campaign_id
        )

        if campaign:
            campaign.amount_raised += donation.amount
            self.campaign_repository.update(campaign)

        return donation

    def get_donation(
        self,
        donation_id: int,
    ) -> Optional[Donation]:

        return self.donation_repository.get_by_id(donation_id)


    def get_all_donations(
        self,
    ) -> list[Donation]:

        return self.donation_repository.get_all()


    def update_donation(
        self,
        donation_id: int,
        request: DonationUpdate,
    ) -> Optional[Donation]:

        donation = self.donation_repository.get_by_id(donation_id)

        if donation is None:
            return None

        updates = request.model_dump(exclude_unset=True)

        for field, value in updates.items():
            setattr(donation, field, value)

        return self.donation_repository.update(donation)


    def delete_donation(
        self,
        donation_id: int,
    ) -> bool:

        return self.donation_repository.delete(donation_id)
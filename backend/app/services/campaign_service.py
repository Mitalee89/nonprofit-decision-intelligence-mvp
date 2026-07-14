from decimal import Decimal
from typing import Optional

from app.models.campaign import Campaign
from app.models.enums import FundStatus
from app.models.fund import Fund
from app.repositories.campaign_repository import CampaignRepository
from app.repositories.fund_repository import FundRepository
from app.schemas.campaign import CampaignCreate, CampaignUpdate


class CampaignService:
    """
    Handles all Campaign business logic.

    Responsibilities:
    - Campaign CRUD
    - Campaign validation
    - Automatic Fund creation
    """

    def __init__(
        self,
        campaign_repository: CampaignRepository,
        fund_repository: FundRepository,
    ):
        self.campaign_repository = campaign_repository
        self.fund_repository = fund_repository

    def create_campaign(
        self,
        request: CampaignCreate,
    ) -> Campaign:

        # Business validation
        if request.start_date > request.end_date:
            raise ValueError(
                "Campaign start date cannot be after end date."
            )

        # Create Campaign
        campaign_data = request.model_dump()

        campaign = Campaign(**campaign_data)

        campaign = self.campaign_repository.create(campaign)

        # Automatically create Fund
        fund = Fund(
            name=f"{campaign.name} Fund",
            campaign_id=campaign.id,
            balance=Decimal("0.00"),
            total_received=Decimal("0.00"),
            status=FundStatus.OPEN,
        )

        self.fund_repository.create(fund)

        return campaign

    def get_campaign(
        self,
        campaign_id: int,
    ) -> Optional[Campaign]:
        return self.campaign_repository.get_by_id(campaign_id)

    def get_all_campaigns(
        self,
    ) -> list[Campaign]:

        return self.campaign_repository.get_all()

    def update_campaign(
        self,
        campaign_id: int,
        request: CampaignUpdate,
    ) -> Optional[Campaign]:

        campaign = self.campaign_repository.get_by_id(campaign_id)

        if campaign is None:
            return None

        updates = request.model_dump(exclude_unset=True)

        # Business validation
        start_date = updates.get("start_date", campaign.start_date)
        end_date = updates.get("end_date", campaign.end_date)

        if start_date > end_date:
            raise ValueError(
                "Campaign start date cannot be after end date."
            )

        for field, value in updates.items():
            setattr(campaign, field, value)

        return self.campaign_repository.update(campaign)

    def delete_campaign(
        self,
        campaign_id: int,
    ) -> bool:

        return self.campaign_repository.delete(campaign_id)

    def get_active_campaigns(
        self,
    ) -> list[Campaign]:

        return self.campaign_repository.get_active_campaigns()
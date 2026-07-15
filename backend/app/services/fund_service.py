from decimal import Decimal
from typing import Optional

from app.models.enums import FundStatus
from app.models.fund import Fund
from app.repositories.fund_repository import FundRepository
from app.schemas.fund import FundUpdate


class FundService:

    def __init__(
        self,
        fund_repository: FundRepository,
    ):
        self.fund_repository = fund_repository

  #  def create_fund(
  #      self,
  #      request: FundCreate,
  #  ) -> Fund:

  #      fund = Fund(
  #          name=request.name,
  #          campaign_id=request.campaign_id,
  #          balance=Decimal("0.00"),
  #          total_received=Decimal("0.00"),
  #          status=FundStatus.OPEN,
  #      )

  #      return self.fund_repository.create(fund)

    def get_fund(
        self,
        fund_id: int,
    ) -> Optional[Fund]:

        return self.fund_repository.get_by_id(fund_id)

    def get_all_funds(
        self,
    ) -> list[Fund]:

        return self.fund_repository.get_all()

    def update_fund(
        self,
        fund_id: int,
        request: FundUpdate,
    ) -> Optional[Fund]:

        fund = self.fund_repository.get_by_id(fund_id)

        if fund is None:
            return None

        updates = request.model_dump(exclude_unset=True)

        for field, value in updates.items():
            setattr(fund, field, value)

        return self.fund_repository.update(fund)

    def delete_fund(
        self,
        fund_id: int,
    ) -> bool:

        return self.fund_repository.delete(fund_id)

    def get_open_funds(
        self,
    ) -> list[Fund]:

        return self.fund_repository.get_open_funds()

    def get_campaign_funds(
        self,
        campaign_id: int,
    ) -> list[Fund]:

        return self.fund_repository.get_by_campaign(campaign_id)
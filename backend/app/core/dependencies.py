from typing import Generator

from fastapi import Depends
from sqlmodel import Session

from app.core.database import engine

from app.repositories.campaign_repository import CampaignRepository
from app.repositories.fund_repository import FundRepository
from app.services.campaign_service import CampaignService


# ------------------------------------------------------------------
# Database Session
# ------------------------------------------------------------------

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


# ------------------------------------------------------------------
# Repositories
# ------------------------------------------------------------------

def get_campaign_repository(
    session: Session = Depends(get_session),
) -> CampaignRepository:
    return CampaignRepository(session)


def get_fund_repository(
    session: Session = Depends(get_session),
) -> FundRepository:
    return FundRepository(session)


# ------------------------------------------------------------------
# Services
# ------------------------------------------------------------------

def get_campaign_service(
    campaign_repository: CampaignRepository = Depends(
        get_campaign_repository
    ),
    fund_repository: FundRepository = Depends(
        get_fund_repository
    ),
) -> CampaignService:

    return CampaignService(
        campaign_repository=campaign_repository,
        fund_repository=fund_repository,
    )
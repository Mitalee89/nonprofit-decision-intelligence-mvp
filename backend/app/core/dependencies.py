from typing import Generator

from fastapi import Depends
from sqlmodel import Session

from app.core.database import engine

from app.repositories.campaign_repository import CampaignRepository
from app.services.campaign_service import CampaignService

from app.repositories.fund_repository import FundRepository
from app.services.fund_service import FundService

from app.repositories.donor_repository import DonorRepository
from app.services.donor_service import DonorService

from app.repositories.donation_repository import DonationRepository
from app.services.donation_service import DonationService

from app.repositories.grant_repository import GrantRepository
from app.services.grant_service import GrantService

from sqlmodel import Session
from fastapi import Depends

from app.core.database import get_session
from app.services.llm_service import LLMService
from app.repositories.donor_match_repository import DonorMatchRepository
from app.services.donor_match_service import DonorMatchService

from app.repositories.grant_match_repository import GrantMatchRepository
from app.services.grant_match_service import GrantMatchService

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

def get_donor_repository(
    session: Session = Depends(get_session),
) -> DonorRepository:
    return DonorRepository(session)

def get_donation_repository(
    session: Session = Depends(get_session),
) -> DonationRepository:
    return DonationRepository(session)

def get_grant_repository(
    session: Session = Depends(get_session),
) -> GrantRepository:
    return GrantRepository(session)

def get_grant_match_repository(
    session: Session = Depends(get_session),
) -> GrantMatchRepository:
    return GrantMatchRepository(session)

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

def get_fund_service(
    repository: FundRepository = Depends(get_fund_repository),
) -> FundService:
    return FundService(repository)

def get_donor_service(
    repository: DonorRepository = Depends(get_donor_repository),
) -> DonorService:
    return DonorService(repository)

def get_donation_service(
    donation_repository: DonationRepository = Depends(get_donation_repository),
    donor_repository: DonorRepository = Depends(get_donor_repository),
    fund_repository: FundRepository = Depends(get_fund_repository),
    campaign_repository: CampaignRepository = Depends(get_campaign_repository),
) -> DonationService:

    return DonationService(
        donation_repository=donation_repository,
        donor_repository=donor_repository,
        fund_repository=fund_repository,
        campaign_repository=campaign_repository,
    )


def get_grant_service(
    repository: GrantRepository = Depends(get_grant_repository),
) -> GrantService:

    return GrantService(repository)

def get_donor_match_service(
    session: Session = Depends(get_session),
    ):
    repository = DonorMatchRepository(session)
    return DonorMatchService(repository)

def get_grant_match_service(
    repository: GrantMatchRepository = Depends(get_grant_match_repository),
) -> GrantMatchService:
    return GrantMatchService(repository)

def get_llm_service(

    campaign_service: CampaignService = Depends(
        get_campaign_service
    ),

    donor_service: DonorService = Depends(
        get_donor_service
    ),

    grant_service: GrantService = Depends(
        get_grant_service
    ),

    donor_match_service: DonorMatchService = Depends(
        get_donor_match_service
    ),

    grant_match_service: GrantMatchService = Depends(
        get_grant_match_service
    ),

):

    return LLMService(

        campaign_service,

        donor_service,

        grant_service,

        donor_match_service,

        grant_match_service,

    )


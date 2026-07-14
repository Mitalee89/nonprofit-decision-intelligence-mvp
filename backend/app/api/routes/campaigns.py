from fastapi import APIRouter, Depends, HTTPException, status

from app.core.dependencies import get_campaign_service
from app.schemas.campaign import (
    CampaignCreate,
    CampaignResponse,
    CampaignUpdate,
)
from app.schemas.common import ApiResponse
from app.services.campaign_service import CampaignService

router = APIRouter(
    prefix="/campaigns",
    tags=["Campaigns"],
)


@router.post(
    "/",
    response_model=ApiResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_campaign(
    request: CampaignCreate,
    campaign_service: CampaignService = Depends(get_campaign_service),
):
    campaign = campaign_service.create_campaign(request)

    return ApiResponse(
        success=True,
        message="Campaign created successfully.",
        data=CampaignResponse.model_validate(campaign),
    )


@router.get(
    "/",
    response_model=ApiResponse,
)
def get_all_campaigns(
    campaign_service: CampaignService = Depends(get_campaign_service),
):
    campaigns = campaign_service.get_all_campaigns()

    return ApiResponse(
        success=True,
        message="Campaigns retrieved successfully.",
        data=[
            CampaignResponse.model_validate(campaign)
            for campaign in campaigns
        ],
    )


@router.get(
    "/{campaign_id}",
    response_model=ApiResponse,
)
def get_campaign(
    campaign_id: int,
    campaign_service: CampaignService = Depends(get_campaign_service),
):
    campaign = campaign_service.get_campaign(campaign_id)

    if campaign is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campaign not found.",
        )

    return ApiResponse(
        success=True,
        message="Campaign retrieved successfully.",
        data=CampaignResponse.model_validate(campaign),
    )


@router.put(
    "/{campaign_id}",
    response_model=ApiResponse,
)
def update_campaign(
    campaign_id: int,
    request: CampaignUpdate,
    campaign_service: CampaignService = Depends(get_campaign_service),
):
    campaign = campaign_service.update_campaign(
        campaign_id,
        request,
    )

    if campaign is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campaign not found.",
        )

    return ApiResponse(
        success=True,
        message="Campaign updated successfully.",
        data=CampaignResponse.model_validate(campaign),
    )


@router.delete(
    "/{campaign_id}",
    response_model=ApiResponse,
)
def delete_campaign(
    campaign_id: int,
    campaign_service: CampaignService = Depends(get_campaign_service),
):
    deleted = campaign_service.delete_campaign(campaign_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campaign not found.",
        )

    return ApiResponse(
        success=True,
        message="Campaign deleted successfully.",
        data={},
    )
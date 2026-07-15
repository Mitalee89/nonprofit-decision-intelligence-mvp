from fastapi import APIRouter, Depends, HTTPException, status

from app.core.dependencies import get_donation_service
from app.schemas.common import ApiResponse
from app.schemas.donation import (
    DonationCreate,
    DonationResponse,
    DonationUpdate,
)
from app.services.donation_service import DonationService

router = APIRouter(
    prefix="/donations",
    tags=["Donations"],
)


@router.post(
    "/",
    response_model=ApiResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_donation(
    request: DonationCreate,
    donation_service: DonationService = Depends(get_donation_service),
):
    try:
        donation = donation_service.create_donation(request)

        return ApiResponse(
            success=True,
            message="Donation created successfully.",
            data=DonationResponse.model_validate(donation),
        )

    except ValueError as ex:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ex),
        )


@router.get(
    "/",
    response_model=ApiResponse,
)
def get_all_donations(
    donation_service: DonationService = Depends(get_donation_service),
):
    donations = donation_service.get_all_donations()

    return ApiResponse(
        success=True,
        message="Donations retrieved successfully.",
        data=[
            DonationResponse.model_validate(donation)
            for donation in donations
        ],
    )


@router.get(
    "/{donation_id}",
    response_model=ApiResponse,
)
def get_donation(
    donation_id: int,
    donation_service: DonationService = Depends(get_donation_service),
):
    donation = donation_service.get_donation(donation_id)

    if donation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Donation not found.",
        )

    return ApiResponse(
        success=True,
        message="Donation retrieved successfully.",
        data=DonationResponse.model_validate(donation),
    )


@router.put(
    "/{donation_id}",
    response_model=ApiResponse,
)
def update_donation(
    donation_id: int,
    request: DonationUpdate,
    donation_service: DonationService = Depends(get_donation_service),
):
    donation = donation_service.update_donation(
        donation_id,
        request,
    )

    if donation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Donation not found.",
        )

    return ApiResponse(
        success=True,
        message="Donation updated successfully.",
        data=DonationResponse.model_validate(donation),
    )


@router.delete(
    "/{donation_id}",
    response_model=ApiResponse,
)
def delete_donation(
    donation_id: int,
    donation_service: DonationService = Depends(get_donation_service),
):
    deleted = donation_service.delete_donation(donation_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Donation not found.",
        )

    return ApiResponse(
        success=True,
        message="Donation deleted successfully.",
        data=None,
    )
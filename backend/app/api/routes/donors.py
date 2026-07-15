from fastapi import APIRouter, Depends, HTTPException, status

from app.core.dependencies import get_donor_service
from app.schemas.common import ApiResponse
from app.schemas.donor import (
    DonorCreate,
    DonorResponse,
    DonorUpdate,
)
from app.services.donor_service import DonorService

router = APIRouter(
    prefix="/donors",
    tags=["Donors"],
)


@router.post(
    "/",
    response_model=ApiResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_donor(
    request: DonorCreate,
    donor_service: DonorService = Depends(get_donor_service),
):
    donor = donor_service.create_donor(request)

    return ApiResponse(
        success=True,
        message="Donor created successfully.",
        data=DonorResponse.model_validate(donor),
    )


@router.get(
    "/",
    response_model=ApiResponse,
)
def get_all_donors(
    donor_service: DonorService = Depends(get_donor_service),
):
    donors = donor_service.get_all_donors()

    return ApiResponse(
        success=True,
        message="Donors retrieved successfully.",
        data=[
            DonorResponse.model_validate(donor)
            for donor in donors
        ],
    )


@router.get(
    "/{donor_id}",
    response_model=ApiResponse,
)
def get_donor(
    donor_id: int,
    donor_service: DonorService = Depends(get_donor_service),
):
    donor = donor_service.get_donor(donor_id)

    if donor is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Donor not found.",
        )

    return ApiResponse(
        success=True,
        message="Donor retrieved successfully.",
        data=DonorResponse.model_validate(donor),
    )


@router.put(
    "/{donor_id}",
    response_model=ApiResponse,
)
def update_donor(
    donor_id: int,
    request: DonorUpdate,
    donor_service: DonorService = Depends(get_donor_service),
):
    donor = donor_service.update_donor(
        donor_id,
        request,
    )

    if donor is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Donor not found.",
        )

    return ApiResponse(
        success=True,
        message="Donor updated successfully.",
        data=DonorResponse.model_validate(donor),
    )


@router.delete(
    "/{donor_id}",
    response_model=ApiResponse,
)
def delete_donor(
    donor_id: int,
    donor_service: DonorService = Depends(get_donor_service),
):
    deleted = donor_service.delete_donor(donor_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Donor not found.",
        )

    return ApiResponse(
        success=True,
        message="Donor deleted successfully.",
        data=None,
    )
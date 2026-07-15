from fastapi import APIRouter, Depends, HTTPException, status

from app.core.dependencies import get_fund_service
from app.schemas.common import ApiResponse
from app.schemas.fund import (
    FundResponse,
    FundUpdate,
)
from app.services.fund_service import FundService

router = APIRouter(
    prefix="/funds",
    tags=["Funds"],
)

@router.get(
    "/",
    response_model=ApiResponse,
)
def get_all_funds(
    fund_service: FundService = Depends(get_fund_service),
):
    funds = fund_service.get_all_funds()

    return ApiResponse(
        success=True,
        message="Funds retrieved successfully.",
        data=[
            FundResponse.model_validate(fund)
            for fund in funds
        ],
    )


@router.get(
    "/{fund_id}",
    response_model=ApiResponse,
)
def get_fund(
    fund_id: int,
    fund_service: FundService = Depends(get_fund_service),
):
    fund = fund_service.get_fund(fund_id)

    if fund is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Fund not found.",
        )

    return ApiResponse(
        success=True,
        message="Fund retrieved successfully.",
        data=FundResponse.model_validate(fund),
    )


@router.put(
    "/{fund_id}",
    response_model=ApiResponse,
)
def update_fund(
    fund_id: int,
    request: FundUpdate,
    fund_service: FundService = Depends(get_fund_service),
):
    fund = fund_service.update_fund(
        fund_id,
        request,
    )

    if fund is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Fund not found.",
        )

    return ApiResponse(
        success=True,
        message="Fund updated successfully.",
        data=FundResponse.model_validate(fund),
    )


@router.delete(
    "/{fund_id}",
    response_model=ApiResponse,
)
def delete_fund(
    fund_id: int,
    fund_service: FundService = Depends(get_fund_service),
):
    deleted = fund_service.delete_fund(fund_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Fund not found.",
        )

    return ApiResponse(
        success=True,
        message="Fund deleted successfully.",
        data=None,
    )
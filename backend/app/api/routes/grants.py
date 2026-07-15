from fastapi import APIRouter, Depends, HTTPException, status

from app.core.dependencies import get_grant_service
from app.schemas.common import ApiResponse
from app.schemas.grant import (
    GrantCreate,
    GrantResponse,
    GrantUpdate,
)
from app.services.grant_service import GrantService

router = APIRouter(
    prefix="/grants",
    tags=["Grants"],
)


@router.post(
    "/",
    response_model=ApiResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_grant(
    request: GrantCreate,
    grant_service: GrantService = Depends(get_grant_service),
):
    grant = grant_service.create_grant(request)

    return ApiResponse(
        success=True,
        message="Grant created successfully.",
        data=GrantResponse.model_validate(grant),
    )


@router.get(
    "/",
    response_model=ApiResponse,
)
def get_all_grants(
    grant_service: GrantService = Depends(get_grant_service),
):
    grants = grant_service.get_all_grants()

    return ApiResponse(
        success=True,
        message="Grants retrieved successfully.",
        data=[
            GrantResponse.model_validate(grant)
            for grant in grants
        ],
    )


@router.get(
    "/{grant_id}",
    response_model=ApiResponse,
)
def get_grant(
    grant_id: int,
    grant_service: GrantService = Depends(get_grant_service),
):
    grant = grant_service.get_grant(grant_id)

    if grant is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Grant not found.",
        )

    return ApiResponse(
        success=True,
        message="Grant retrieved successfully.",
        data=GrantResponse.model_validate(grant),
    )


@router.put(
    "/{grant_id}",
    response_model=ApiResponse,
)
def update_grant(
    grant_id: int,
    request: GrantUpdate,
    grant_service: GrantService = Depends(get_grant_service),
):
    grant = grant_service.update_grant(
        grant_id,
        request,
    )

    if grant is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Grant not found.",
        )

    return ApiResponse(
        success=True,
        message="Grant updated successfully.",
        data=GrantResponse.model_validate(grant),
    )


@router.delete(
    "/{grant_id}",
    response_model=ApiResponse,
)
def delete_grant(
    grant_id: int,
    grant_service: GrantService = Depends(get_grant_service),
):
    deleted = grant_service.delete_grant(grant_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Grant not found.",
        )

    return ApiResponse(
        success=True,
        message="Grant deleted successfully.",
        data=None,
    )
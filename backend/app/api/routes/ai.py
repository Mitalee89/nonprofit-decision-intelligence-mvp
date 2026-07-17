import traceback

from fastapi import APIRouter, Depends, HTTPException

from app.core.dependencies import get_llm_service
from app.services.llm_service import LLMService

from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


@router.post("/recommend-donors/{campaign_id}")
def recommend_donors(
    campaign_id: int,
    llm_service: LLMService = Depends(get_llm_service),
):
    try:
        result = llm_service.recommend_donors(campaign_id)

        return {
        "success": True,
        "message": "Donor recommendations generated successfully.",
        "data": jsonable_encoder(result),
        }

    except ValueError as ex:

        raise HTTPException(
            status_code=404,
            detail=str(ex),
        )

    

    except Exception as ex:
        traceback.print_exc()
        raise HTTPException(
        status_code=500,
        detail=str(ex),
    )
from pydantic import BaseModel, Field


class DonorRecommendation(BaseModel):
    donor_id: int = Field(..., description="Recommended donor ID")
    confidence: int = Field(..., ge=0, le=100)
    reasoning: str


class DonorRecommendationResponse(BaseModel):
    recommendations: list[DonorRecommendation]
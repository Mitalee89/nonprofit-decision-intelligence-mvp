import json
from typing import Type

from app.llm.models import DonorRecommendationResponse
from app.llm.models import GrantRecommendationResponse

from app.llm.models import (
    DonorRecommendationResponse,
    GrantRecommendationResponse,
)


from typing import Type

def parse_recommendations(
    response: str,
    response_model: Type,
):

    data = json.loads(response)

    if isinstance(data, list):
        data = {
            "recommendations": data
        }

    if "recommendations" not in data:
        raise ValueError("LLM response missing recommendations.")

    for recommendation in data["recommendations"]:

        if (
            "confidence_score" not in recommendation
            and "confidence" in recommendation
        ):
            recommendation["confidence_score"] = recommendation["confidence"]

    data["recommendations"].sort(
        key=lambda x: x["confidence_score"],
        reverse=True,
    )

    data["recommendations"] = data["recommendations"][:5]

    return response_model.model_validate(data)
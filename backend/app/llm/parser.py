import json

from app.llm.models import (
    DonorRecommendationResponse,
)


def parse_recommendations(
    response: str,
):

    data = json.loads(response)

    if isinstance(data, list):

        data = {

            "recommendations": data

        }

    if "recommendations" not in data:

        raise ValueError(
            "LLM response missing recommendations."
        )
    data["recommendations"].sort(
        key=lambda x: x["confidence_score"],
        reverse=True,
    )
    data["recommendations"] = data["recommendations"][:5]
    return DonorRecommendationResponse.model_validate(
        data
    )
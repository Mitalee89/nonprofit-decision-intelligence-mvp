from urllib import response

from app.llm.client import generate
from app.llm.parser import parse_recommendations
from app.llm.prompts import donor_recommendation_prompt
from app.llm.models import DonorRecommendationResponse


def recommend_donors(
    campaign: dict,
    donors: list[dict],
):
    """
    Runs donor recommendation through the LLM.

    Returns:
        DonorRecommendationResponse
    """

    prompt = donor_recommendation_prompt(
        campaign,
        donors,
    )

    response = generate(prompt)


    recommendations = parse_recommendations(
        response, DonorRecommendationResponse,
    )

    return recommendations
from urllib import response

from app.llm.client import generate
from app.llm.parser import parse_recommendations
from app.llm.prompts import grant_recommendation_prompt
from app.llm.models import GrantRecommendationResponse


def recommend_grants(
    campaign: dict,
    grants: list[dict],
):
    """
    Runs grant recommendation through the LLM.

    Returns:
        GrantRecommendationResponse
    """

    prompt = grant_recommendation_prompt(
        campaign,
        grants,
    )

    response = generate(prompt)


    recommendations = parse_recommendations(
        response, GrantRecommendationResponse,
    )

    return recommendations
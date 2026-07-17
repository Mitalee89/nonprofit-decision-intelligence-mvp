from app.models.grant_match import GrantMatch
from app.repositories.grant_match_repository import (
    GrantMatchRepository,
)


class GrantMatchService:

    def __init__(
        self,
        grant_match_repository: GrantMatchRepository,
    ):
        self.grant_match_repository = grant_match_repository

    def replace_matches(
        self,
        campaign_id: int,
        recommendations,
    ):

        self.grant_match_repository.delete_by_campaign(
            campaign_id
        )

        saved = []

        for recommendation in recommendations:

            match = GrantMatch(

                campaign_id=campaign_id,

                grant_id=recommendation.grant_id,

                confidence_score=float(
                    recommendation.confidence
                ),

                reasoning=recommendation.reasoning,

            )

            saved.append(

                self.grant_match_repository.create(
                    match
                )

            )

        return saved

    def get_matches(
        self,
        campaign_id: int,
    ):

        return self.grant_match_repository.get_by_campaign(
            campaign_id
        )
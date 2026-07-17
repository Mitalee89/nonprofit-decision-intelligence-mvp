from app.models.donor_match import DonorMatch
from app.repositories.donor_match_repository import (
    DonorMatchRepository,
)


class DonorMatchService:

    def __init__(
        self,
        donor_match_repository: DonorMatchRepository,
    ):
        self.donor_match_repository = donor_match_repository

    def replace_matches(
        self,
        campaign_id: int,
        recommendations,
    ):

        self.donor_match_repository.delete_by_campaign(
            campaign_id
        )

        saved = []

        for recommendation in recommendations:

            match = DonorMatch(

                campaign_id=campaign_id,

                donor_id=recommendation.donor_id,

                confidence_score=float(
                    recommendation.confidence
                ),

                reasoning=recommendation.reasoning,

            )

            saved.append(

                self.donor_match_repository.create(
                    match
                )

            )

        return saved

    def get_matches(
        self,
        campaign_id: int,
    ):

        return self.donor_match_repository.get_by_campaign(
            campaign_id
        )
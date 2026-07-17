from app.llm.donor_matcher import recommend_donors
from app.llm.serializers import campaign_to_llm, donors_to_llm

from app.services.campaign_service import CampaignService
from app.services.donor_service import DonorService
from app.services.donor_match_service import DonorMatchService


class LLMService:

    def __init__(
        self,
        campaign_service: CampaignService,
        donor_service: DonorService,
        donor_match_service: DonorMatchService,
    ):
        self.campaign_service = campaign_service
        self.donor_service = donor_service
        self.donor_match_service = donor_match_service

    def recommend_donors(self, campaign_id: int):

        print("========== AI DONOR MATCHING ==========")

        # Step 1
        print("Loading campaign...")
        campaign = self.campaign_service.get_campaign(campaign_id)

        if campaign is None:
            raise ValueError(f"Campaign {campaign_id} not found.")

        print(f"Campaign loaded: {campaign.name}")

        # Step 2
        print("Loading active donors...")
        donors = self.donor_service.get_all_donors()

        if not donors:
            raise ValueError("No active donors found.")

        print(f"{len(donors)} donors found")

        # Step 3
        print("Serializing campaign...")
        campaign_data = campaign_to_llm(campaign)

        print("Serializing donors...")
        donor_data = donors_to_llm(donors)

        # Step 4
        print("Calling Ollama...")
        llm_response = recommend_donors(
            campaign_data,
            donor_data,
        )

        print("LLM completed")

        # Step 5
        print("Saving donor matches...")
        saved_matches = self.donor_match_service.replace_matches(
            campaign_id,
            llm_response.recommendations,
        )

        print(f"{len(saved_matches)} matches saved")

        donor_lookup = {
            donor.id: donor
            for donor in donors
        }

        result = []

        for match in saved_matches:

            donor = donor_lookup.get(match.donor_id)

            result.append(
                {
                    "donor_id": match.donor_id,
                    "donor_name": donor.name if donor else "",
                    "confidence_score": match.confidence_score,
                    "reasoning": match.reasoning,
                }
            )

        print("========== AI COMPLETE ==========")

        return result
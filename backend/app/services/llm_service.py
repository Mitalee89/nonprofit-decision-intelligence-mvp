from app.llm.donor_matcher import recommend_donors
from app.llm.serializers import campaign_to_llm, donors_to_llm

from app.services import campaign_service
from app.services import donor_service
from app.services import donor_match_service   
from app.services import grant_service
from app.llm.grant_matcher import recommend_grants
from app.llm.serializers import grants_to_llm


class LLMService:

    def __init__(
        self,
        campaign_service,
        donor_service,
        grant_service,
        donor_match_service,
        grant_match_service,
):

        self.campaign_service = campaign_service
        self.donor_service = donor_service
        self.grant_service = grant_service
        self.donor_match_service = donor_match_service
        self.grant_match_service = grant_match_service

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
    
    def recommend_grants(self, campaign_id: int):

            print("========== AI GRANT MATCHING ==========")

            # Step 1
            print("Loading campaign...")
            campaign = self.campaign_service.get_campaign(campaign_id)

            if campaign is None:
                raise ValueError(f"Campaign {campaign_id} not found.")

            print(f"Campaign loaded: {campaign.name}")

            # Step 2
            print("Loading active grants...")
            grants = self.grant_service.get_all_grants()

            if not grants:
                raise ValueError("No active grants found.")

            print(f"{len(grants)} grants found")

            # Step 3
            print("Serializing campaign...")
            campaign_data = campaign_to_llm(campaign)

            print("Serializing grants...")
            grant_data = grants_to_llm(grants)

            # Step 4
            print("Calling Ollama...")
            llm_response = recommend_grants(
                campaign_data,
                grant_data,
            )

            print("LLM completed")

            # Step 5
            print("Saving grant matches...")
            saved_matches = self.grant_match_service.replace_matches(
                campaign_id,
                llm_response.recommendations,
            )

            print(f"{len(saved_matches)} matches saved")

            grant_lookup = {
                grant.id: grant
                for grant in grants
            }

            result = []

            for match in saved_matches:

                grant = grant_lookup.get(match.grant_id)

                result.append(
                    {
                        "grant_id": match.grant_id,
                        "grant_name": grant.title if grant else "",
                        "confidence_score": match.confidence_score,
                        "reasoning": match.reasoning,
                    }
                )

            print("========== AI COMPLETE ==========")

            return result
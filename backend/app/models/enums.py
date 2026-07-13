from enum import Enum


class CampaignStatus(str, Enum):
    DRAFT = "Draft"
    ACTIVE = "Active"
    COMPLETED = "Completed"
    CLOSED = "Closed"


class FundStatus(str, Enum):
    ACTIVE = "Active"
    CLOSED = "Closed"


class DonationStatus(str, Enum):
    RECEIVED = "Received"
    ALLOCATED = "Allocated"
    REFUNDED = "Refunded"


class GrantStatus(str, Enum):
    OPEN = "Open"
    UNDER_REVIEW = "Under Review"
    ASSIGNED = "Assigned"
    CLOSED = "Closed"
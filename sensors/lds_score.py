def calculate_lds_score(
    divergence: float,          # D: 0.0–1.0
    infrastructure_lag: float,  # I: 0.0–1.0
    temporal_offset: float,     # T: 0.0–1.0
    supply_tier: float,         # S: 0.0–1.0
    cultural_filter: float,     # C: 0.0–1.0
    validation_support: float   # V: 0.0–1.0
) -> float:
    """
    Calculates the Logistic Disparity Score (LDS).
    Higher scores suggest greater likelihood of memory drift due to logistic disparity.
    """
    numerator = divergence * (infrastructure_lag + temporal_offset + supply_tier + cultural_filter)
    denominator = 1 + validation_support
    return round(numerator / denominator, 3)

def compute_usaa_score(paternalism, complexity, institution_bias, protective):
    """
    Combines four sensor scores into a symbolic system diagnosis.
    Scores expected to be integers from 0 (none) to 4 (high).
    """

    total = paternalism + complexity + institution_bias + protective

    # Symbolic scoring tiers
    if total >= 12:
        classification = "delusional_critical"
        suggestion = "System redesign needed. Current structure disempowers and obscures."
    elif total >= 8:
        classification = "extractive_but_aware"
        suggestion = "Improvements possible with transparency and empowerment adjustments."
    elif total >= 5:
        classification = "marginally_adaptive"
        suggestion = "Mixed signals. Consider simplifying and decentralizing authority."
    elif total >= 2:
        classification = "adaptive_under_constraints"
        suggestion = "Reasonable structure. Monitor intent clarity and maintain checks."
    else:
        classification = "optimal_symbiotic"
        suggestion = "System promotes clarity, autonomy, and mutual benefit."

    return {
        "total_score": total,
        "classification": classification,
        "recommendation": suggestion
    }

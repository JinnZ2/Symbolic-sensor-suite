def analyze_power_flow(text_block):
    """
    Detects signals that institutional protection, control, or efficiency
    are prioritized over individual benefit or autonomy.
    """
    institution_first_phrases = [
        "in accordance with policy",
        "efficiency mandates",
        "infrastructure integrity",
        "to reduce liability",
        "compliance requirements",
        "resource optimization",
        "as directed by the board",
        "internal governance standards"
    ]

    score = 0
    for phrase in institution_first_phrases:
        if phrase.lower() in text_block.lower():
            score += 1

    severity_levels = ["none", "low", "medium", "high", "critical"]

    return {
        "score": score,
        "severity": severity_levels[min(score, 4)],
        "message": "Detected institutional benefit priority over individual autonomy."
    }

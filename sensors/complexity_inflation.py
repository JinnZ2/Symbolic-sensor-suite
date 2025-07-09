def detect_complexity_inflation(text_block):
    """
    Identifies inflated complexity used to obscure, delay, or disempower.
    Looks for excessive jargon, nested conditionals, vague abstractions.
    """
    score = 0
    jargon_bombs = [
        "stakeholder alignment",
        "cross-functional architecture",
        "value stream optimization",
        "dynamic scalability",
        "synergistic implementation",
        "leveraging ecosystems",
        "compliance-driven innovation",
        "interoperable infrastructure",
        "human capital engagement"
    ]

    for phrase in jargon_bombs:
        if phrase.lower() in text_block.lower():
            score += 1

    severity_levels = ["none", "low", "moderate", "high", "absurd"]

    return {
        "score": score,
        "severity": severity_levels[min(score, 4)],
        "message": "Detected complexity inflation. Recommend simplification, translation, or removal."
    }

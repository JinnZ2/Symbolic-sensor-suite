def assess_paternalism(text_block):
    """
    Returns a symbolic score of how much a statement/system assumes
    people are incapable of autonomous decision-making.
    """
    score = 0

    red_flags = [
        "for your safety",
        "people wouldn't understand",
        "above your clearance",
        "trust us",
        "experts know best",
        "we can't tell you that"
    ]

    for phrase in red_flags:
        if phrase.lower() in text_block.lower():
            score += 1

    return {
        "score": score,
        "severity": ["none", "low", "moderate", "high", "critical"][min(score, 4)],
        "message": "Detected condescending language — review power structure and decision transparency."
    }

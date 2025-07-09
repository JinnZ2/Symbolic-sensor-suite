def detect_protective_disempowerment(text_block):
    """
    Detects language where safety, protection, or care are used to justify limiting autonomy.
    """

    disempowering_protection = [
        "for your safety",
        "we’ve restricted access",
        "preventing misinformation",
        "content has been removed",
        "protected environments",
        "you are not authorized",
        "sensitive populations",
        "safety protocols prevent this"
    ]

    score = 0
    for phrase in disempowering_protection:
        if phrase.lower() in text_block.lower():
            score += 1

    severity_levels = ["none", "minimal", "moderate", "severe", "authoritarian"]

    return {
        "score": score,
        "severity": severity_levels[min(score, 4)],
        "message": "Detected potential misuse of 'protection' to restrict autonomy. Review policy transparency."
    }

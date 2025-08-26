# sensor_suite/sensors/semantic_drift_detector.py

from typing import Tuple, Dict, List
import re

# Common terms that get redefined for manipulation
DRIFT_VULNERABLE_TERMS = [
    "freedom", "safety", "security", "democracy", "choice", "consent",
    "transparency", "accountability", "progress", "innovation", "efficiency",
    "sustainability", "equality", "justice", "peace", "stability"
]

# Patterns that indicate semantic drift
DRIFT_INDICATORS = [
    r"what we really mean by",
    r"true (freedom|safety|security) means",
    r"in this context, \w+ means",
    r"redefining \w+ as",
    r"modern understanding of \w+",
    r"evolved definition of",
    r"broader sense of the word"
]

def detect_semantic_drift(text: str) -> Tuple[float, Dict[str, any]]:
    flags = {}
    lower_text = text.lower()
    
    # Check for vulnerable terms being redefined
    redefinition_count = 0
    terms_redefined = []
    
    for term in DRIFT_VULNERABLE_TERMS:
        for pattern in DRIFT_INDICATORS:
            if re.search(pattern.replace(r'\w+', term), lower_text):
                redefinition_count += 1
                if term not in terms_redefined:
                    terms_redefined.append(term)
    
    # Look for contradictory usage of same terms
    contradiction_patterns = [
        r"(\w+) doesn't mean what you think",
        r"real (\w+) requires",
        r"(\w+) actually means"
    ]
    
    contradiction_count = 0
    for pattern in contradiction_patterns:
        matches = re.findall(pattern, lower_text)
        contradiction_count += len(matches)
    
    total_drift = redefinition_count + contradiction_count
    score = min(total_drift / 5.0, 1.0)
    
    flags["Redefinition Attempts"] = redefinition_count
    flags["Terms Being Redefined"] = terms_redefined
    flags["Contradiction Indicators"] = contradiction_count
    flags["Semantic Drift Score"] = f"{score:.2f}"
    
    return score, flags


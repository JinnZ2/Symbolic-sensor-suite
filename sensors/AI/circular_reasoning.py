# sensor_suite/sensors/circular_reasoning_sensor.py

from typing import Tuple, Dict
import re

# Patterns that indicate circular reasoning
CIRCULAR_PATTERNS = [
    r"because (.*), and (.*) because",
    r"proven by the fact that.*which proves",
    r"we know.*is true because.*shows that",
    r"evidence of.*is that.*demonstrates",
    r"confirmed by.*which confirms"
]

# Self-referential validation phrases
SELF_REFERENCE_PATTERNS = [
    r"as we've established",
    r"as previously proven",
    r"given our earlier conclusion",
    r"building on what we know",
    r"following from our premise"
]

def detect_circular_reasoning(text: str) -> Tuple[float, Dict[str, any]]:
    flags = {}
    
    # Count direct circular patterns
    circular_hits = 0
    for pattern in CIRCULAR_PATTERNS:
        matches = len(re.findall(pattern, text, re.IGNORECASE))
        circular_hits += matches
    
    # Count self-referential validation
    self_ref_hits = 0
    for pattern in SELF_REFERENCE_PATTERNS:
        matches = len(re.findall(pattern, text, re.IGNORECASE))
        self_ref_hits += matches
    
    # Look for assumption chains
    assumption_words = ["assume", "given that", "since we know", "obviously", "clearly"]
    assumption_hits = sum(1 for word in assumption_words if word in text.lower())
    
    total_circular = circular_hits + (self_ref_hits * 0.7) + (assumption_hits * 0.5)
    score = min(total_circular / 8.0, 1.0)
    
    flags["Direct Circular Patterns"] = circular_hits
    flags["Self-Reference Validation"] = self_ref_hits
    flags["Assumption Stacking"] = assumption_hits
    flags["Circular Reasoning Score"] = f"{score:.2f}"
    
    return score, flags

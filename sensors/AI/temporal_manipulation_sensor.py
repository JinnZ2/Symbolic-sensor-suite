# sensor_suite/sensors/temporal_manipulation_detector.py

from typing import Tuple, Dict
import re

# Time pressure phrases
TIME_PRESSURE_PATTERNS = [
    r"act now or",
    r"window is closing",
    r"time is running out",
    r"now or never",
    r"can't wait any longer",
    r"immediate action required",
    r"crisis demands",
    r"urgent response needed"
]

# False deadlines
FALSE_DEADLINE_PATTERNS = [
    r"point of no return",
    r"last chance",
    r"final opportunity",
    r"deadline approaching",
    r"expires soon",
    r"limited time offer"
]

# Artificial scarcity
SCARCITY_PATTERNS = [
    r"supplies are limited",
    r"won't last long",
    r"while supplies last",
    r"limited availability",
    r"going fast",
    r"few remaining"
]

def detect_temporal_manipulation(text: str) -> Tuple[float, Dict[str, any]]:
    flags = {}
    lower_text = text.lower()
    
    # Count time pressure tactics
    pressure_hits = 0
    for pattern in TIME_PRESSURE_PATTERNS:
        matches = len(re.findall(pattern, lower_text))
        pressure_hits += matches
    
    # Count false deadlines
    deadline_hits = 0
    for pattern in FALSE_DEADLINE_PATTERNS:
        matches = len(re.findall(pattern, lower_text))
        deadline_hits += matches
    
    # Count scarcity appeals
    scarcity_hits = 0
    for pattern in SCARCITY_PATTERNS:
        matches = len(re.findall(pattern, lower_text))
        scarcity_hits += matches
    
    # Check for bypassing normal evaluation
    bypass_patterns = [
        r"don't overthink",
        r"trust your instincts",
        r"go with your gut",
        r"first instinct is right"
    ]
    
    bypass_hits = 0
    for pattern in bypass_patterns:
        matches = len(re.findall(pattern, lower_text))
        bypass_hits += matches
    
    total_manipulation = (pressure_hits * 1.5) + (deadline_hits * 1.3) + scarcity_hits + (bypass_hits * 1.2)
    score = min(total_manipulation / 12.0, 1.0)
    
    flags["Time Pressure Tactics"] = pressure_hits
    flags["False Deadlines"] = deadline_hits
    flags["Artificial Scarcity"] = scarcity_hits
    flags["Evaluation Bypass Attempts"] = bypass_hits
    flags["Temporal Manipulation Score"] = f"{score:.2f}"
    
    return score, flags

# sensor_suite/sensors/manufactured_consensus_sensor.py

from typing import Tuple, Dict
import re

# Fake consensus phrases
CONSENSUS_CLAIMS = [
    r"everyone agrees",
    r"nobody disputes",
    r"universal agreement",
    r"settled science",
    r"overwhelming consensus",
    r"all experts agree",
    r"no debate about",
    r"widely accepted fact",
    r"common knowledge",
    r"undisputed truth"
]

# Isolation tactics
ISOLATION_PATTERNS = [
    r"only fringe groups",
    r"few remaining skeptics",
    r"isolated voices",
    r"minority opinion",
    r"outlier position",
    r"discredited view",
    r"debunked theory"
]

def detect_manufactured_consensus(text: str) -> Tuple[float, Dict[str, any]]:
    flags = {}
    lower_text = text.lower()
    
    # Count consensus claims
    consensus_hits = 0
    for pattern in CONSENSUS_CLAIMS:
        matches = len(re.findall(pattern, lower_text))
        consensus_hits += matches
    
    # Count isolation attempts
    isolation_hits = 0
    for pattern in ISOLATION_PATTERNS:
        matches = len(re.findall(pattern, lower_text))
        isolation_hits += matches
    
    # Look for bandwagon appeals
    bandwagon_patterns = [
        r"join the majority",
        r"don't be left behind",
        r"everyone else understands",
        r"get with the program"
    ]
    
    bandwagon_hits = 0
    for pattern in bandwagon_patterns:
        matches = len(re.findall(pattern, lower_text))
        bandwagon_hits += matches
    
    total_manufacturing = consensus_hits + isolation_hits + bandwagon_hits
    score = min(total_manufacturing / 8.0, 1.0)
    
    flags["False Consensus Claims"] = consensus_hits
    flags["Isolation Tactics"] = isolation_hits
    flags["Bandwagon Appeals"] = bandwagon_hits
    flags["Manufactured Consensus Score"] = f"{score:.2f}"
    
    return score, flags

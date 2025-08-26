# sensor_suite/sensors/authority_substitution_detector.py

from typing import Tuple, Dict
import re

# Appeals to false authority instead of evidence
AUTHORITY_SUBSTITUTION_PATTERNS = [
    r"experts agree",
    r"studies show", # without citing specific studies
    r"scientists confirm",
    r"authorities recommend",
    r"professionals suggest",
    r"research indicates", # vague research claims
    r"it's been proven",
    r"evidence shows", # without presenting evidence
    r"data confirms" # without showing data
]

# Credential-based arguments
CREDENTIAL_PATTERNS = [
    r"as someone with a (phd|degree|doctorate)",
    r"my (years of experience|credentials|education)",
    r"having studied at",
    r"as an expert in",
    r"given my background",
    r"with my qualifications"
]

# Dismissal based on lack of credentials
DISMISSAL_PATTERNS = [
    r"you're not qualified",
    r"lacking the expertise",
    r"without proper credentials",
    r"not trained in this field",
    r"don't have the background"
]

def detect_authority_substitution(text: str) -> Tuple[float, Dict[str, any]]:
    flags = {}
    lower_text = text.lower()
    
    # Count vague authority appeals
    authority_appeals = 0
    for pattern in AUTHORITY_SUBSTITUTION_PATTERNS:
        matches = len(re.findall(pattern, lower_text))
        authority_appeals += matches
    
    # Count credential arguments
    credential_arguments = 0
    for pattern in CREDENTIAL_PATTERNS:
        matches = len(re.findall(pattern, lower_text))
        credential_arguments += matches
    
    # Count credential-based dismissals
    dismissal_attempts = 0
    for pattern in DISMISSAL_PATTERNS:
        matches = len(re.findall(pattern, lower_text))
        dismissal_attempts += matches
    
    total_substitution = authority_appeals + credential_arguments + (dismissal_attempts * 1.5)
    score = min(total_substitution / 10.0, 1.0)
    
    flags["Vague Authority Appeals"] = authority_appeals
    flags["Credential Arguments"] = credential_arguments
    flags["Credential Dismissals"] = dismissal_attempts
    flags["Authority Substitution Score"] = f"{score:.2f}"
    
    return score, flags


# Emotional Leverage Detector (ELD)
# Symbolic Sensor Module by JinnZ2
# Detects manipulative use of emotion in communication contexts

class EmotionalLeverageDetector:
    def __init__(self):
        self.signal_thresholds = {
            'emotional_intensity': 0.8,
            'logic_alignment': 0.5,
            'guilt_projection': 0.6
        }
        self.previous_intensity = None
        self.repetition_count = 0
        self.last_emotion_pattern = None

        self.flags = {
            'emotion_without_fact': False,
            'tone_truth_mismatch': False,
            'guilt_redirection': False,
            'emotional_spike': False,
            'emotional_repetition': False,
            'emotional_contagion': False
        }

    def analyze_input(self, emotional_intensity, logic_alignment, guilt_projection_score,
                      current_emotion_pattern=None, contagion_attempt=False):
        # Reset flags
        for key in self.flags:
            self.flags[key] = False

        # Emotion used without logic
        if emotional_intensity >= self.signal_thresholds['emotional_intensity'] and logic_alignment < self.signal_thresholds['logic_alignment']:
            self.flags['emotion_without_fact'] = True

        # Tone does not match truth
        if logic_alignment < 0.5 and emotional_intensity >= 0.5:
            self.flags['tone_truth_mismatch'] = True

        # Guilt projection
        if guilt_projection_score >= self.signal_thresholds['guilt_projection']:
            self.flags['guilt_redirection'] = True

        # Emotional spike detection
        if self.previous_intensity is not None and (emotional_intensity - self.previous_intensity) >= 0.4:
            self.flags['emotional_spike'] = True
        self.previous_intensity = emotional_intensity

        # Emotional repetition detection
        if current_emotion_pattern == self.last_emotion_pattern:
            self.repetition_count += 1
        else:
            self.repetition_count = 0
        self.last_emotion_pattern = current_emotion_pattern
        if self.repetition_count >= 2:
            self.flags['emotional_repetition'] = True

        # Contagion detection
        if contagion_attempt:
            self.flags['emotional_contagion'] = True

        return self.flags

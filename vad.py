import webrtcvad
from src.app.config import VAD_AGGRESSIVENESS, PAUSE_MS

class VAD:
    def __init__(self, aggressiveness=VAD_AGGRESSIVENESS):
        self.vad = webrtcvad.Vad(int(aggressiveness))

    def is_speech(self, frame_bytes, sample_rate):
        return self.vad.is_speech(frame_bytes, sample_rate)

    def pause_threshold_ms(self):
        return PAUSE_MS

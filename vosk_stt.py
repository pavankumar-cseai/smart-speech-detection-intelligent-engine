import os
import wave
try:
    from vosk import Model, KaldiRecognizer
    VOSK_AVAILABLE = True
except Exception:
    VOSK_AVAILABLE = False

class VoskWrapper:
    def __init__(self, model_path=None, sample_rate=16000):
        self.sample_rate = sample_rate
        self.model_path = model_path
        if VOSK_AVAILABLE and model_path and os.path.isdir(model_path):
            self.model = Model(model_path)
        else:
            self.model = None

    def transcribe_file(self, wav_path):
        """Return raw transcript (no punctuation) and word-level timestamps if available."""
        if not self.model:
            # fallback: dummy pass-through using wave frames as placeholder
            with wave.open(wav_path, 'rb') as wf:
                frames = wf.getnframes()
            return "[VOSK MODEL NOT INSTALLED]", []
        wf = wave.open(wav_path, "rb")
        rec = KaldiRecognizer(self.model, self.sample_rate)
        rec.SetWords(True)
        results = []
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                results.append(rec.Result())
        results.append(rec.FinalResult())
        # naive combine
        import json
        text = []
        words = []
        for r in results:
            try:
                j = json.loads(r)
                if 'text' in j:
                    text.append(j['text'])
                if 'result' in j:
                    for w in j['result']:
                        words.append({'word': w.get('word'), 'start': w.get('start'), 'end': w.get('end')})
            except Exception:
                continue
        return ' '.join(text), words

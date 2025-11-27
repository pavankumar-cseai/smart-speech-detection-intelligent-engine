import time
from src.asr.vosk_stt import VoskWrapper
from src.process.disfluency import remove_fillers
from src.process.repetition import dedupe_repetition
from src.process.punctuate import naive_punctuate
from src.process.grammar import apply_grammar_corrections
from src.process.style import apply_style
from src.app.config import ASR_MODEL_PATH

class Pipeline:
    def __init__(self, asr_model_path=ASR_MODEL_PATH):
        self.asr = VoskWrapper(asr_model_path)

    def process_file(self, wav_path, style='neutral'):
        timings = {}
        t0 = time.time()
        raw_text, words = self.asr.transcribe_file(wav_path)
        timings['asr'] = time.time() - t0

        t1 = time.time()
        no_fillers = remove_fillers(raw_text)
        timings['disfluency'] = time.time() - t1

        t2 = time.time()
        deduped = dedupe_repetition(no_fillers)
        timings['repetition'] = time.time() - t2

        t3 = time.time()
        punctuated = naive_punctuate(deduped)
        timings['punctuate'] = time.time() - t3

        t4 = time.time()
        gram = apply_grammar_corrections(punctuated)
        timings['grammar'] = time.time() - t4

        t5 = time.time()
        styled = apply_style(gram, style=style)
        timings['style'] = time.time() - t5

        timings['total'] = time.time() - t0
        return styled, timings

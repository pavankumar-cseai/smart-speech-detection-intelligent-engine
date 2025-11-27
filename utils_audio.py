import soundfile as sf
def read_wav(path, expected_sr=16000):
    data, sr = sf.read(path)
    if sr != expected_sr:
        # simple resample using scipy
        from scipy.signal import resample
        import numpy as np
        new_len = int(len(data) * expected_sr / sr)
        data = resample(data, new_len)
        sr = expected_sr
    return data, sr

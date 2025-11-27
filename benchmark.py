import time
from src.process.pipeline import Pipeline

def run_benchmark(wav_path, style='neutral'):
    p = Pipeline()
    start = time.time()
    out, timings = p.process_file(wav_path, style=style)
    end = time.time()
    print('Result:', out[:200])
    print('Timings (ms):', {k:int(v*1000) for k,v in timings.items()})
    print('Total (ms):', int((end-start)*1000))

if __name__=='__main__':
    import sys
    if len(sys.argv)<2:
        print('Usage: python benchmark.py examples/example_audio.wav')
    else:
        run_benchmark(sys.argv[1])

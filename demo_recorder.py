# Simple demo recorder that records from default microphone and saves WAV file.
import sounddevice as sd
import soundfile as sf

def record(filename='examples/example_audio.wav', duration=5, samplerate=16000):
    print('Recording for', duration, 'seconds...')
    data = sd.rec(int(duration*samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    sf.write(filename, data, samplerate)
    print('Saved to', filename)

if __name__=='__main__':
    record()

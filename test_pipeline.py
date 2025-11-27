from src.process.pipeline import Pipeline

def test_pipeline_runs():
    p = Pipeline()
    # Use small synthetic sample - pipeline should not crash. We don't assert output correctness here.
    styled, timings = p.process_file('examples/example_audio.wav')
    assert isinstance(styled, str)
    assert 'total' in timings

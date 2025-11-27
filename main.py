from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from src.process.pipeline import Pipeline
from src.app.server_utils import pretty_timings

app = FastAPI(title="Intelligent Dictation Engine ")

pipeline = Pipeline()

class ProcessRequest(BaseModel):
    style: str = "neutral"

@app.post("/process/full")
async def process_full(style: str = "neutral", file: UploadFile = File(...)):
    """Accepts a WAV file upload and runs full pipeline synchronously."""
    data = await file.read()
    # write temporary file
    import tempfile, os
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    tmp.write(data)
    tmp.flush()
    tmp.close()
    result, timings = pipeline.process_file(tmp.name, style=style)
    try:
        os.remove(tmp.name)
    except Exception:
        pass
    return {"result": result, "timings_ms": pretty_timings(timings)}

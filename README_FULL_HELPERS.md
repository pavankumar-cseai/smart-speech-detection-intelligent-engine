Additional notes:
- To get Vosk running, download a small Vosk model and place it in `models/` and update ASR_MODEL_PATH in src/app/config.py.
- To replace language_tool with GECToR or another edit-based GEC, see docs/design.md and integrate ONNX model in src/process/grammar.py.

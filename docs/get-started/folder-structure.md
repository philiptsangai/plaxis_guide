# Project Structure

A minimal layout mirroring the training workflow used in this guide:

```
AI_PLAXIS_training/
├── plaxis/
│   ├── inputs_all.json
│   ├── input.json
│   ├── soils_total.json
│   └── plaxis.py
├── run_plaxis_AI_training.py
└── plaxis_log.json     # auto‑created
```

- **`input.json`** – single run configuration (geometry, materials, stages).
- **`inputs_all.json`** – list of runs for batching/parametric studies.
- **`soils_total.json`** – shared material library.
- **`plaxis.py`** – automation functions called by the runner.
- **`run_plaxis_AI_training.py`** – orchestrates batch execution + logging.
- **`plaxis_log.json`** – appended by the runner with results + status.

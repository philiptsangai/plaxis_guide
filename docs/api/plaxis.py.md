# `plaxis.py` — API Reference

Each function below includes: **signature**, **parameters**, **returns**, and a **Try this** snippet.

## `connect(host: str, port: int, password: str)`
- **Returns:** `(s, g)` server + global handles.
- **Notes:** one place to set timeouts, retries, and logging of connection info.

## `build_model(cfg: dict, s, g) -> dict`
- **Parameters:** `cfg["geometry"]`, `cfg["materials"]`…
- **Returns:** model summary dict.

## `run_calculation(cfg: dict, s, g) -> dict`
- **Does:** define phases/stages, run, wait, collect outputs.

## `export_results(cfg: dict, s, g, out_dir: str) -> dict`
- **Does:** extract selected results to CSV/JSON; return summary stats.

!!! tip "Pattern"
    Keep functions pure. Avoid global state beyond the `s, g` handles.

!!! example "Open the example code"
    Browse the example implementation shipped with this guide at  
    `docs/assets/code/AI_PLAXIS_training/plaxis/plaxis.py`

"""Batch runner example for PLAXIS training runs.
This is a teaching scaffold.
"""
import json, time
from pathlib import Path
from datetime import datetime
from assets.code.AI_PLAXIS_training.plaxis.plaxis import connect, build_model, run_calculation, export_results

ROOT = Path(__file__).resolve().parent
PLAXIS_DIR = ROOT / "plaxis"
LOG_PATH = ROOT / "plaxis_log.json"

def load_json(p): return json.loads(Path(p).read_text())

def append_log(entry):
    log = []
    if LOG_PATH.exists():
        try:
            log = json.loads(LOG_PATH.read_text())
        except Exception:
            log = []
    log.append(entry)
    LOG_PATH.write_text(json.dumps(log, indent=2))

def run_one(cfg, s, g):
    build = build_model(cfg, s, g)
    results = run_calculation(cfg, s, g)
    export = export_results(cfg, s, g, out_dir=str(ROOT / "outputs"))
    return {"build": build, "results": results, "export": export}

def main():
    all_cfg = load_json(PLAXIS_DIR / "inputs_all.json")
    s, g = connect(password="your_password")
    try:
        for i, cfg in enumerate(all_cfg.get("runs", []), 1):
            t0 = time.time()
            status = "ok"
            try:
                out = run_one(cfg, s, g)
            except Exception as e:
                status = "error"
                out = {"error": str(e)}
            dt = round(time.time() - t0, 2)
            append_log({
                "run_id": cfg.get("id", f"run_{i}"),
                "project": cfg.get("project"),
                "status": status,
                "duration_s": dt,
                "timestamp": datetime.utcnow().isoformat() + "Z",
                **out
            })
    finally:
        try: s.close()
        except Exception: pass

if __name__ == "__main__":
    main()

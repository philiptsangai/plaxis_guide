# Batching & Logging

Pattern used in this guide:
1. Load `inputs_all.json` (list of runs).
2. For each item, call into `plaxis.py` with a single `input.json`‑like dict.
3. Append results (or errors) to `plaxis_log.json` with timestamps & run id.

```python
# pseudo
for cfg in inputs_all:
    try:
        result = run_one(cfg)
        log.append({**summary(result), "status": "ok"})
    except Exception as e:
        log.append({"run_id": cfg["id"], "status": "error", "msg": str(e)})
```

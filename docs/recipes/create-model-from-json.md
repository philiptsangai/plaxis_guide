# Create Model from JSON

Minimal flow using the included example files:

```python
from pathlib import Path
import json
from assets.code.AI_PLAXIS_training.plaxis.plaxis import connect, build_model, run_calculation, export_results

cfg = json.loads(Path('docs/assets/code/AI_PLAXIS_training/plaxis/input.json').read_text())
s, g = connect(password='your_password')
build = build_model(cfg, s, g)
results = run_calculation(cfg, s, g)
export = export_results(cfg, s, g, out_dir='outputs')
s.close()
```

!!! note "Try this"
    Start with a tiny `input.json` (single material, short length) to validate the pipeline before scaling.

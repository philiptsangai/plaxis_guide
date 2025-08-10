"""Example PLAXIS 3D automation helpers.
This is a teaching scaffold; adapt to your project before production use.
"""
from pathlib import Path
from datetime import datetime
import json

try:
    from plxscripting.easy import new_server
except Exception:
    # Allow docs to build without PLAXIS installed
    new_server = None

def connect(host='localhost', port=10000, password=''):
    if new_server is None:
        raise RuntimeError("plxscripting not available in this environment")
    s, g = new_server(host, port, password=password)
    return s, g

def build_model(cfg, s, g):
    """Create geometry, materials, mesh.
    Returns a summary dict.
    """
    geom = cfg.get('geometry', {})
    mats = cfg.get('materials', {})
    # Pseudocode – replace with actual PLAXIS commands, e.g. g.tunnel(...)
    summary = {
        "diameter_m": geom.get("diameter_m"),
        "length_m": geom.get("length_m"),
        "material": mats.get("soil"),
        "created_at": datetime.utcnow().isoformat() + "Z"
    }
    return summary

def run_calculation(cfg, s, g):
    """Define phases and run calculation. Returns results summary."""
    staging = cfg.get('staging', [])
    # Pseudocode; fill in with g.phase(), g.calculate(), etc.
    return {
        "phases": [st.get("name") for st in staging],
        "status": "completed"
    }

def export_results(cfg, s, g, out_dir='outputs'):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    # Pseudocode: export nodal displacements etc.
    results = {"ux": 0.0, "uy": 0.0, "uz": 0.0}
    (Path(out_dir) / f"{cfg.get('project','run')}_results.json").write_text(json.dumps(results, indent=2))
    return results

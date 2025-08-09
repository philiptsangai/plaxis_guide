# Config Schema (Draft)

**Top level**

| Key | Type | Required | Notes |
|---|---|---:|---|
| `project` | string | ✓ | slug for outputs |
| `geometry` | object | ✓ | tunnel, alignment, lengths |
| `materials` | object | ✓ | references `soils_total.json` |
| `staging` | array | ✓ | ordered list of phases |
| `outputs` | array |  | e.g., `["ux","uy","uz","sigma1"]` |

**Geometry**
```json
{
  "diameter_m": 6.0,
  "length_m": 50.0,
  "axis": [0, 0, 1],
  "start_xyz": [0, 0, 0]
}
```

**Materials**
- `"soil"`: key name referring to `soils_total.json`
- Optional project‑specific overrides, e.g. `{"E50_MPa": 30}`

**Staging**
```json
[{ "name": "exc_1", "advance_m": 1.0 }]
```

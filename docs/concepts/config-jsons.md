# Config JSONs

Keep JSON structures **explicit** and **typed**. Suggested top‑level keys:

```json
{
  "project": "ex01_simple_tunnel",
  "geometry": { "diameter_m": 6.0, "length_m": 50.0 },
  "materials": { "soil": "Silty Sand", "E50_MPa": 25 },
  "staging": [{ "name": "exc_1", "advance_m": 1.0 }],
  "outputs": ["ux", "uy", "uz", "sigma1"]
}
```

See **Reference → Config Schema** for a precise schema + examples.

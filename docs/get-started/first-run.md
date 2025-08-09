# First Run

Minimal handshake to confirm the PLAXIS remote server works:

```python
# try_plaxis_handshake.py
from plxscripting.easy import new_server
s, g = new_server('localhost', 10000, password='your_password')
print(g.version)
s.close()
```

If you see a version string printed, you're set. Next, run the simplest end‑to‑end recipe in **Recipes → Create Model from JSON**.

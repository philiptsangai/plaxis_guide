# Remote Scripting

- Connect once, reuse the session.
- Use `g` for commands (global) and `s` for server control.
- Prefer **idempotent** functions: re‑running should not corrupt state.
- Validate connection; fail fast with helpful error messages.

```python
from plxscripting.easy import new_server

def connect(host='localhost', port=10000, password=''):
    s, g = new_server(host, port, password=password)
    return s, g
```

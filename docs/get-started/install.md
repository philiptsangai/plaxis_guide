# Install & Setup (PLAXIS 3D) — Steps 1–3

## Before you start
- Windows 10/11
- **PLAXIS 3D** installed (CONNECT/2023+ with Remote Scripting)
- We’ll use the PLAXIS **Python Distribution** interpreter (or your own env)

> PLAXIS exposes a Remote Scripting server and a Python wrapper (`plxscripting`). We’ll use that to automate PLAXIS 3D from Python.

---

## Step 1 — Install an IDE (VS Code)

1. Download and install **Visual Studio Code** for Windows.
2. Open VS Code → create/open a working folder (e.g. `plaxis3d-automation`).
3. (Optional) Install the **Python** extension when prompted.

---

## Step 2 — Activate the PLAXIS Python environment in VS Code

Use the interpreter that ships with PLAXIS so you don’t worry about dependencies.

**Common interpreter paths (adjust for your version):**
```
C:\ProgramData\Bentley\Geotechnical\PLAXIS Python Distribution V2\python\python.exe
```
or (newer Seequent branding):
```
C:\ProgramData\Seequent\PLAXIS Python Distribution V2\python\python.exe
```

**In VS Code:**
1. Press **Ctrl+Shift+P** → **Python: Select Interpreter**.
2. Choose **Enter interpreter path…** and browse to the PLAXIS Python `python.exe` above.
3. Open VS Code **Terminal**; it should now use that interpreter.

> Alternative: use your own env (Conda/venv) and run `pip install plxscripting`.

---

## Step 3 — Connect to the PLAXIS 3D API (start server + handshake)

We’ll launch **PLAXIS 3D Input** with the scripting server, then connect via `new_server`.

The project includes a ready script at `docs/assets/code/connect_plaxis3d.py`:

```python
import subprocess, time
from plxscripting.easy import new_server

# Adjust path to your installed version:
PLAXIS3D_PATH = r"C:\Program Files\Bentley\Geotechnical\PLAXIS 3D CONNECT Edition V22\Plaxis3DInput.exe"
# Example for 2023.x under Seequent branding:
# PLAXIS3D_PATH = r"C:\Program Files\Seequent\PLAXIS 3D 2023.2\Plaxis3DInput.exe"

PORT_INPUT  = 10000
PASSWORD    = "MyStrongPwd123"

# Start PLAXIS 3D with the scripting server enabled
subprocess.Popen(
    [PLAXIS3D_PATH, f"--AppServerPassword={PASSWORD}", f"--AppServerPort={PORT_INPUT}"],
    shell=False
)
time.sleep(5)  # give PLAXIS time to boot

# Connect to the server
s_i, g_i = new_server("localhost", PORT_INPUT, password=PASSWORD)

# Smoke test
print("Connected. PLAXIS version:", g_i.version)
g_i.gotostructures()   # harmless command to prove the session is live
s_i.close()
```

**Run it from the VS Code terminal:**
```bash
python docs/assets/code/connect_plaxis3d.py
```

You should see PLAXIS 3D open (SERVER ACTIVE) and a version string printed in the terminal.

### Quick Troubleshooting
- **Connection error / timeout** → Ensure the server is active, and your `PORT_INPUT` + `PASSWORD` match.
- **Executable path differs** → Adjust `PLAXIS3D_PATH` for your installed version/vendor (“Bentley” vs “Seequent”).
- **Using your own Python env** → `pip install plxscripting` and re-run.

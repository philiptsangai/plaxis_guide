# First Run (Handshake Verification)

Use the tiny script created in **Install & Setup → Step 3** to verify everything is wired up.

**Run:**
```bash
python docs/assets/code/connect_plaxis3d.py
```

**Expected:**
- PLAXIS 3D opens (or focuses if already open) and shows **SERVER ACTIVE**.
- Terminal prints: `Connected. PLAXIS version: <version>`
- No errors → you’re ready to build models and run calculations from Python.

> Tip: If PLAXIS is already open, you can enable the server from within PLAXIS and just run the `new_server(...)` part to connect.

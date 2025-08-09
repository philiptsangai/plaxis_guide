# Install & Setup

## 1) Python environment
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 2) PLAXIS Remote Scripting
- Ensure PLAXIS 3D is installed with the Python Remote Scripting interface.
- Enable the remote server (localhost, default port) in PLAXIS 3D.
- Verify connectivity with a short handshake (see *First Run*).

!!! note
    You do **not** need a web server. This documentation site can be hosted free on GitHub Pages or shipped as an offline HTML bundle.

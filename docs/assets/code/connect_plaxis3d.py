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

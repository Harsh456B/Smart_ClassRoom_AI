import subprocess
import sys
import time

print("🚀 Starting Smart Classroom AI System...")

# Start recognition system
print("📷 Starting Camera + AI Recognition...")
recognize_process = subprocess.Popen(
    [sys.executable, "recognize.py"]
)

# Small delay so camera starts first
time.sleep(5)

# Start dashboard
print("📊 Starting Live Dashboard...")
dashboard_process = subprocess.Popen(
    ["streamlit", "run", "dashboard/app.py"]
)

try:
    recognize_process.wait()
    dashboard_process.wait()
except KeyboardInterrupt:
    print("\n🛑 Stopping system...")
    recognize_process.terminate()
    dashboard_process.terminate()

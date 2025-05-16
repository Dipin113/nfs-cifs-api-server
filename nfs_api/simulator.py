import threading, time, os

TARGET_DIR = "/exports/data"
_running = False
_thread = None

def simulate_changes():
    global _running
    start_time = time.time()
    while _running and (time.time() - start_time < 60):
        ts = str(int(time.time()))
        folder = os.path.join(TARGET_DIR, f"folder_{ts}")
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, f"file_{ts}.txt"), "w") as f:
            f.write(f"Created at {ts}")
        time.sleep(1)
        
        with open(os.path.join(folder, f"file_{ts}.txt"), "a") as f:
            f.write(f"\nUpdated at {int(time.time())}")
        time.sleep(1)
        os.system(f"rm -rf {folder}")
        time.sleep(2)

def start_simulation():
    global _running, _thread
    if _running:
        return {"message": "Simulation already running"}
    _running = True
    _thread = threading.Thread(target=simulate_changes)
    _thread.start()
    return {"message": "Simulation started"}

def stop_simulation():
    global _running
    _running = False
    return {"message": "Simulation stopping"}

def simulation_status():
    return _running

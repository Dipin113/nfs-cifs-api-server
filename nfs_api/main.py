from fastapi import FastAPI
from nfs_api.simulator import start_simulation, stop_simulation, simulation_status
from nfs_api.utils import create_file, update_file, delete_file

app = FastAPI(
    title="NFS Simulation API",
    description="Control and simulate file changes on an NFS server through RESTful API endpoints.",
    version="1.0.0"
)

@app.get("/status", tags=["Simulation"])
def status():
    return {"running": simulation_status()}

@app.post("/start", tags=["Simulation"])
def start():
    return start_simulation()

@app.post("/stop", tags=["Simulation"])
def stop():
    return stop_simulation()

@app.post("/create", tags=["File Operations"])
def create(name: str):
    return create_file(name)

@app.post("/update", tags=["File Operations"])
def update(name: str):
    return update_file(name)

@app.post("/delete", tags=["File Operations"])
def delete(name: str):
    return delete_file(name)

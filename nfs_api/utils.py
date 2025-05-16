import os

TARGET_DIR = "/exports/data"

def create_file(name: str):
    path = os.path.join(TARGET_DIR, name)
    with open(path, "w") as f:
        f.write(f"Created: {name}")
    return {"created": name}

def update_file(name: str):
    path = os.path.join(TARGET_DIR, name)
    if not os.path.exists(path):
        return {"error": "File does not exist"}
    with open(path, "a") as f:
        f.write(f"\nUpdated: {name}")
    return {"updated": name}

def delete_file(name: str):
    path = os.path.join(TARGET_DIR, name)
    if os.path.exists(path):
        os.remove(path)
        return {"deleted": name}
    return {"error": "File not found"}

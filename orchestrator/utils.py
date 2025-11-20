import os

def save_log(content: str, filename: str = "run.log"):
    log_dir = os.path.join(os.path.dirname(__file__), "..", "data", "logs")
    os.makedirs(log_dir, exist_ok=True)
    with open(os.path.join(log_dir, filename), "a", encoding="utf-8") as f:
        f.write(content + "\n")

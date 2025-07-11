from threading import Lock
import os

lock = Lock()
file_path = "count.txt"
TICKET_CAP = 2000

# Load ticket count from file if exists
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        _ticket_count = int(f.read().strip())
else:
    _ticket_count = 0

def update_count(num):
    global _ticket_count
    with lock:
        _ticket_count += num
        with open(file_path, "w") as f:
            f.write(str(_ticket_count))

def get_count():
    return _ticket_count

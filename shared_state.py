from threading import Lock

lock = Lock()
_ticket_count = 26  # Set this to your current real sold ticket count
TICKET_CAP = 2000

def update_count(num):
    global _ticket_count
    with lock:
        _ticket_count += num

def get_count():
    return _ticket_count

import time
import hashlib

def cpu_work(duration=15):
    start = time.time()
    i = 0

    while time.time() - start < duration:
        hashlib.sha256(str(i).encode()).hexdigest()
        i += 1

if __name__ == "__main__":
    cpu_work()


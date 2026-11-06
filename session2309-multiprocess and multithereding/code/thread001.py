import threading
import time

def task(name):
    print(f"Task {name} started.")
    time.sleep(5)
    print(f"Task {name} finished.")

#task("Eating")
#task("Drinking")

t1 = threading.Thread(target=task, args = ("Eating",))
t2 = threading.Thread(target=task, args = ("Drinking",))

t1.start()
t2.start()

t1.join()
t2.join()



import threading

"""
Threading request
"""
# def do_request():
#     while True:
#         response = requests.post('www.google.com', data=data).text
#         print(response)
#
#
# threads = []
# for i in range(50):
#     t = threading.Thread(target=do_request)
#     t.daemon = True
#     threads.append(t)
#
# for i in range(50):
#     threads[i].start()
#
# for i in range(50):
#     threads[i].join()
#
"""
Using Lock for object with context
"""


class Counter():
    def __init__(self):
        self.lock = threading.Lock()
        self.count = 0

    def increment(self):
        with self.lock:
            self.count += 1


def worker(sensor_index, items, counter):
    for _ in range(items):
        # Read from the sensor
        # ...
        counter.increment()


def run_threads(func, items, counter):
    threads = []
    for i in range(5):
        args = (i, items, counter)
        thread = threading.Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


items = 100000
counter = Counter()
run_threads(worker, items, counter)
print(f'Counter should be {5 * items}, found {counter.count}')
"""
Importing the threading module
"""

lock = threading.Lock()
deposit = 100


# Function to add profit to the deposit
def add_profit():
    global deposit
    for i in range(100000):
        lock.acquire()
        deposit = deposit + 10
        lock.release()


# Function to deduct money from the deposit
def pay_bill():
    global deposit
    for i in range(100000):
        lock.acquire()
        deposit = deposit - 10
        lock.release()


# Creating threads
thread1 = threading.Thread(target=add_profit, args=())
thread2 = threading.Thread(target=pay_bill, args=())
# Starting the threads
thread1.start()
thread2.start()
# Waiting for both the threads to finish executing
thread1.join()
thread2.join()
# Displaying the final value of the deposit
print(deposit)

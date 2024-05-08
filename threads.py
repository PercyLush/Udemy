import time
from threading import Thread


def ask_user():
    start = time.time()
    user_input = input("Enter your Name: ")
    greet = f"Hello, {user_input}"
    print(greet)
    print(f"ask_user = {time.time() - start}")


def complex_calculation():
    start = time.time()
    print("Starting Calculation...")
    [x**2 for x in range(20000000)]
    print(f"complex_calculation = {time.time() - start}")

start = time.time()
ask_user()
complex_calculation()
print(f"\nSingle Thread Total Time: {time.time() - start}")
    

Thread1 = Thread(target=ask_user)
Thread2 = Thread(target=complex_calculation)

start = time.time()
Thread1.start()
Thread2.start()

Thread1.join()
Thread2.join()

print(f"Two Threads Total Time: {time.time() - start}")

import time

def fibonacci(terms):
    global s
    s = time.perf_counter()
    first=0
    second=1

    for i in range(2,terms):
        third = first + second
        first=second
        second=third

        if (time.perf_counter() - s) > 5:
            print("Inside Condition")
            return third % 10

    return third % 10


terms=int(input("enter no of terms\n"))
print(fibonacci(terms))
print((time.perf_counter() - s))
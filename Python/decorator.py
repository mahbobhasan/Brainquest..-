def timer(func):
    def inner():
        print("start")
        func()
        print("Time end")
    return inner
def get_factorial():
    print("factorial")

timer(get_factorial)()

@timer
def get_multiplier():
    print("Multiplier")

get_multiplier()
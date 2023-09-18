import time


def timer(func) -> int:
    def wrapper(*args, **kwargs):
        # Record the start time
        start_time = time.time()
        func()
        # Record the end time
        end_time = time.time()
        # Calculate and return the elapsed time
        elapsed_time = end_time - start_time
        return elapsed_time

    return wrapper


@timer
def hi() -> str:
    for _ in range(1000000):
        pass


def main():
    print(hi())


if __name__ == "__main__":
    main()
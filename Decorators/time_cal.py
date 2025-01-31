import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() 
        result = func(*args, **kwargs)  
        end_time = time.time()  
        time_taken = end_time - start_time  
        print(f"Time taken for {func.__name__}: {time_taken:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def time_operation():
    print("Operation started...")
    time.sleep(2)  
    print("Operation completed.")

time_operation()



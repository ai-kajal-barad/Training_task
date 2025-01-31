# First decorator 
def print_stars(func):
    def wrapper(*args, **kwargs):
        print("*****")
        result = func(*args, **kwargs)
        print("*****")
        return result
    return wrapper

# Second decorator 
def print_percent(func):
    def wrapper(*args, **kwargs):
        print("%%%%%")
        result = func(*args, **kwargs)
        print("%%%%%")
        return result
    return wrapper

@print_stars
@print_percent
def print_message():
    print("KAJAL")

print_message()

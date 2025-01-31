'''5. Write a program to create a list of numbers, and extract integer numbers from a list based on the
below conditions.
a. The number must be 4 digits long i.e (1000 to 9999)
b. The second digit of the number must be odd and the last digit must be even.
c. The number must be divisible by either 8 or 5.'''

def extract_num(input_num):
    result = []
    for num in input_num:
        if isinstance(num, int) and 1000 <= num <= 9999:
            if int(str(num)[1]) % 2 != 0 and int(str(num)[-1]) % 2 == 0:
                if num % 8 == 0 or num % 5 == 0:
                    result.append(num)
    return result

while True:
    try:
        number_list = list(map(int, input("Enter numbers separated by spaces (or type 'exit' to quit): ").split()))
        result = extract_num(number_list)
        print("Filtered Numbers:", result)
    except ValueError:
        print("Exiting program...")
        break

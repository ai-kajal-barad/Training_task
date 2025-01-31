'''Write a program to extract string elements from a list based on the conditions below.
a. The first character must be lower and consonant.
b. The string must not contain any number and also does not contain any special character'''

def extract_str():
	vowels = 'aeiou'
	input_str=[]
	result = []
	while True:
		user_input=input("please enter string(stop for exit):")
		if user_input == 'stop':
			break
		input_str.append(user_input)
	for item in input_str:
		if isinstance(item, str):
			if item[0].islower() and item[0] not in vowels and item[0].isalpha():
				if item.isalpha():
					result.append(item)
	return result
	
ex_str = extract_str()
print(ex_str)

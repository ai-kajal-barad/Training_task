'''2.Function to check if a given number is an Armstrong number or not, a function must return a boolean.'''
def armstrong(num):
	s=0
	temp=int(num)
	while int(num) >0:
		r= int(num) % 10
		s=s+(r*r*r)
		num  =int(num) / 10
	if temp==s:
		return True
	else:
		return False

number=armstrong(input("please enter number: "))
print(number)

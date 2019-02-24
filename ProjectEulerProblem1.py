'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 

The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def main():
	value = 0;
	total = 0; 
	while (value < 1000):
		if (((value)%(3) == 0) or ((value)%(5) == 0)):
			total = total + value
		value = value + 1
	print(total)
#call to main
main()
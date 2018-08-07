def main():
	FibonacciNumber1 = 1
	FibonacciNumber2 = 1
	SumOfFibonacciNumbers= 0 #Up to four million
	while (FibonacciNumber1 < 4000000 or FibonacciNumber2 < 4000000):
		FibonacciNumber1 = FibonacciNumber1 + FibonacciNumber2
		if ((FibonacciNumber1%2) == 0):
			SumOfFibonacciNumbers = SumOfFibonacciNumbers + FibonacciNumber1
		if (FibonacciNumber1 > 4000000 or FibonacciNumber2 > 4000000):
			break
		FibonacciNumber2 = FibonacciNumber1 + FibonacciNumber2
		if ((FibonacciNumber2%2) == 0):
			SumOfFibonacciNumbers = SumOfFibonacciNumbers + FibonacciNumber2
	print(SumOfFibonacciNumbers)
#call to main
main()
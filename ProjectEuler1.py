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
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def checkDivisor(num):
    for j in range(1,21):
        if (num%j != 0):
            return "false"
    return "true"
    
def main():
    correctDivisor = [2432902008176640000]
    for i in range(0,100):
        for k in range(2,10000):
            x = checkDivisor(correctDivisor[i]/k)
            if (x == "true"):
                correctDivisor.append(correctDivisor[i]/k)
                break
        print(correctDivisor)
    
main()


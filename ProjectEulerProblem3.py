'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

import re

#Source: https://stackoverflow.com/questions/567222/simple-prime-generator-in-python
def isprime(n):
    return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None

def main():
    num = 600851475143
    primeList = [x for x in range(10000) if isprime(x)]
    newList = []
    print(primeList)
    for i in range(0,1000):
        if ((num)%(primeList[i]) == 0):
            num = num/primeList[i]
            newList.append(primeList[i])
            i = 0
    print(max(newList))
    print(num)
    
#call to main
main()
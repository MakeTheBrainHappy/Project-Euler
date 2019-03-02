"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 equals 91 times 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def main():
    numList = []
    for i in range(100,1000):
        for j in range(100,1000):
            numList.append(i*j)
    #Source: https://www.w3schools.com/python/python_howto_remove_duplicates.asp
    numList = list(set(numList))
    numList.sort()
    palinList = []
    for j in range (0,len(numList)):
        if (len(str(numList[j])) == 5):
            if ((str(numList[j])[0] == str(numList[j])[4]) and (str(numList[j])[1] != str(numList[j])[3])):
                palinList.append(numList[j])
        if (len(str(numList[j])) == 6):
            if (str(numList[j])[0] == str(numList[j])[5] and (str(numList[j])[1] == str(numList[j])[4]) and str(numList[j])[2] == str(numList[j])[3]):
                palinList.append(numList[j])
    print(palinList)       
    
main()

# Q3. Write a program to print all the prime numbers till 100.

def isPrime(num):
    fact=0
    for i in range(1,(num+1)):
        if(num%i==0):
            fact+=1
    return (fact==2)

for i in range(1,100):
    if(isPrime(i)):
        print(i)

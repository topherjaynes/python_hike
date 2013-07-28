#recusrion practice
import timeit

'''
Think of the base case!
'''

#countdown keeps calling it self till we hit the base case
def countdown(n):
    #basecase
    if n <= 0:
        print 'blastoff!'
    else:
        print n
        countdown(n-1)

# recursive example of Fib
# F(n) = F(n-1) + F(n-2)
# prints the nth digit of Fib
# why doesn't this perform well? Write out the tree and see duplicate nodes
def fibonacci(n):
    #basecases
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1)+fibonacci(n-2)

'''
How can we optimize?
Calculate from the bottom
This is o(n)
'''
def opt_fib(n):
    if n < 2:
        return n
    else:
        fibNMinusOne = 1
        fibNMinusTwo = 0
        fibN = 0
        #need to add one here because it stops one short on n
        for i in range(2,n+1):
            fibN = fibNMinusOne + fibNMinusTwo
            fibNMinusTwo = fibNMinusOne
            fibNMinusOne = fibN
        return fibN

'''
Implement recursive method reverse() that takes a nonnegative integer as 
input and prints the digits of n vertically, starting with the low-order digit'''

def reverse(n):
    if n < 10:
        print n
    else:
        #print last digit
        print n%10
        #remove last digit
        reverse(n//10)
'''
this solution uses floor division, which I never heard of. Talked simliar with %
>>> 123456//100
1234
>>> 123456%100
56
>>> t = 123456
>>> print t//10,t%10
12345 6
>>>
'''        


if __name__ == '__main__':
    #countdown(10)
    #print fibonacci(1)
    #print opt_fib(1)
    reverse(1234567)
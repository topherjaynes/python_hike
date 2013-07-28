#recusrion practice
import timeit

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
    result = [0,1]
    if n < 2:
        return result[n]
    else:
        fibNMinusOne = 1
        fibNMinusTwo = 0
        fibN = 0
        #need to add one here because it stops one short on n
        for i in range(2,n+1):
            fibN = fibNMinusOne + fibNMinusTwo
            fibNMinusTwo = fibNMinusOne
            fibNMinusOne = fibN
            print fibN
        return fibN
            


if __name__ == '__main__':
    #countdown(10)
    print fibonacci(10)
    print opt_fib(10)
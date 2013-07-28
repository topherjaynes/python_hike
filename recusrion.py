#recusrion practice

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

def fibonacci(n):
    #basecases
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1)+fibonacci(n-2)


if __name__ == '__main__':
    #countdown(10)
    print fibonacci(6)
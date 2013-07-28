'''
@notes
Generator - http://docs.python.org/2/tutorial/classes.html#generators

Generators are a simple and powerful tool for creating iterators.

http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained/231855#231855
http://stackoverflow.com/questions/101268/hidden-features-of-python/101310#101310

Similiar to list comprehensions

! @returns a generator object, which meats that it is iterable
Can only be interated over one(?)
'''
def str_reverse():
    test =" This is a string"

    def reverse(data):
        for index in range(len(data)-1,-1,-1):
            yield data[index]

    print_obj(test)
'''
String mapping
takes a list of nums and converts to str
'''
def str_map(list):
    s = (str(num) for num in list)
    print_ob(s)

#print generator object
def print_ob(gener):
    for i in gener:
        print i

'''
Expressions, making them more succint 
'''

#sum of squares

def sum_sqr(x):
    print sum(i*i for i in range(x))



def main():
    #str_reverse()
    #sum_sqr(10)
    str_map([1,2,3])

if __name__ == "__main__":
    main()
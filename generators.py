'''
Generator - http://docs.python.org/2/tutorial/classes.html#generators

Generators are a simple and powerful tool for creating iterators.
'''

test =" This is a string"

def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

#print test
for i in reverse(test):
    print i
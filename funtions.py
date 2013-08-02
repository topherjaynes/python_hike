'''
maximize code reuse!

def creates and object and assignes it a name

while lambda returns a result

arguments are passed by assignement

'''


# comments

def test2():
    print 'hey!'


'''
polymorphic, basically anythign that supports the * will work in a function that is dynamically typed
'''

# scopes
'''
Referes to the value's visibilty. name space created
happens at assignment time
'''

# names are contained in defs


def scopetest():
    x = 'will this be seen outside?'
    # hint, no

# print x
'''
Traceback (most recent call last):
  File "funtions.py", line 34, in <module>
    print x
NameError: name 'x' is not defined
'''

# since the scope is within def, we can reuse x


def scopetest2():
    # if the scope allowed us to access it we should see the previous string
    # print x
    # throws UnboundLocalError: local variable 'x' referenced before assignment
    x = "this is a different string!"
    print x


'''
each module is a 'global' scope
attrributes of the object
Global, doesn't mean GLOBAL, more module'
'''
if __name__ == '__main__':
    scopetest2()

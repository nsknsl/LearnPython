#20170220

#Scopes and Namespace Example

def scope_test():
    def do_local():
        spam = 'local spam'
    
    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'
    
    def do_global():
        global spam
        spam = 'global spam'
        print("see->", spam)
    spam = 'stst spam'
    do_local()
    print("after local assinment:", spam)
    do_nonlocal()
    print("After nonlocal assinment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

x = 0
def outer():
    x = 1
    def inner():
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

# inner: 2
# outer: 1
# global: 0

x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

# inner: 2
# outer: 2
# global: 0
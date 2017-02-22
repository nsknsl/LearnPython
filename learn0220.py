#20170220

#Module
# when you run a python module with
# python fibo.py <arguments>
# the code in the module will be
# executed just as if you imported it,
# but with the __name__ set to "__main__"
# that means that by adding this code at the 
# end of your module

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

# the built-in function dir() is used to find out names a module defines.

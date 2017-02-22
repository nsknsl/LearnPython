#20170222
# private Variables

""" “Private” instance variables that cannot be accessed except from 
inside an object don’t exist in Python. However, there is a convention 
that is followed by most Python code: a name prefixed with an underscore 
(e.g. _spam) should be treated as a non-public part of the API 
(whether it is a function, a method or a data member). 
It should be considered an implementation detail and subject 
to change without notice. """

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
    
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
    
    __update = update

class MappingSubclass(Mapping):

    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)

d = MappingSubclass("gg")
print(d.items_list)
ii = ["hh","rr"]
yy = [2,6]
d.update(ii,yy)
print(d.items_list)

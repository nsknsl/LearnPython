#20170222




class Animal:
    """ To learn or not to learn """
    def __init__(self):
        print("init animal")
        self.name = ""
    def give_name(self,name):
        print("give name ")
        self.name = name


class has_legs:
    """ To learn or not to learn """
    def __init__(self):
        print("init has_legs")
        self.legs = True
    def give_legs(self, num_legs):
        print("give legs")
        self.num_legs = num_legs


class dog(Animal,has_legs):
    """ To learn or not to learn """
    def __init__(self):
        print("init Dog")
        self.is_dog = True
    def run(self, how_far):
        self.run_distance = how_far
        print("Begin to run")


d = dog()
d.give_name("bigbig")
d.give_legs(4)
d.run(20)

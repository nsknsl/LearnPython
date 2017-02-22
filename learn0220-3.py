#20170220
#Class and Class Objects

class Myclass:
    """hey"""
    i = 123
    def f(self):
        return 'hello world'

#references:
print(Myclass.i)
Myclass.i = 567
print(Myclass.i)
x = Myclass()
print(x.i)


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)

k = Myclass()

kf = k.f

for i in range(5):
    print(kf())
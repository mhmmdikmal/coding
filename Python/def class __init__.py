class mipa:
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
     # adding two objects
    def __add__(self, other):
        return self.a + other.a, self.b + other.b 
 
Ob1 = mipa(1, 2)
Ob2 = mipa(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)

# Python program to overload
# a comparison operators
 
class A:
    def __init__(self, a):
        self.a = a
    def __gt__(self, other):
        if(self.a>other.a):
            return True
        else:
            return False
ob1 = A(2)
ob2 = A(3)

if(ob1>ob2):
    print("\nob1 is greater than ob2")
else:
    print("\nob2 is greater than ob1")
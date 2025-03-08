"""class A1:
    pass
class A2:
    pass
class B(A1,A2):
    pass
"""

class A1:
    def method_a1(self):
        print("Method from A1")
class A2:
    def method_a2(self):
        print("Method from A2")
class B(A1,A2):
    def method_b(self):
        print("Method from B")
b=B()
b.method_a1()
b.method_a2()
b.method_b()

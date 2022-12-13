class A:
    def feature1(self):
        print("f1 working")

    def feature2(self):
        print("f2 working")

class B(A):
    def feature3(self):
        print("f3 working")
    def feature4(self):
        print("f4 working")

class C(B):
    def feature5(self):
        print("f5 working")



a1 = A()
a2 = B()
a3 = C()
a1.feature1()
a2.feature2()
a3.feature3()
a2.feature4()
a3.feature4()
class A:
    def fn1(self):
        print("fn1 of A")
    def fn2(self):
        print("fn2 of A")

class B:
    def fn1(self):
        print("fn1 of B")
    def fn3(self):
        print("fn3 of B")


class C(B,A):
    def fn4(self):
        print("fn of class C")


obj=C()

obj.fn1()
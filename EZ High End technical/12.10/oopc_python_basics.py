class one():#grandf
    def fun1(self):
        print("fun1")
    def fun2(self):
        print("fun2")
class two(one):#father
    def fun3(self):
        print("fun3")
    def fun4(self):
        print("fun4")
class three():
    def fun5(self):
        print("fun5")
obj=one()
obj1=two()
obj2=three()
obj1.fun()


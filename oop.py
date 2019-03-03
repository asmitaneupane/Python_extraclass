class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # def show(self): it is buildin function which can print. we can use display or whatever..
    def print(self):
        print(self.name,"is",self.age,"years old")
        # print("Age is",self.age)

obj = Dog("Goofy",3)
# obj.show()
# print(obj.age)
# print(obj.name)
obj.print()

obj1 = Dog("Tommy",5)
obj1.print()




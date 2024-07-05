'''
Inheritance - 
'''
class Parent: 
   def __init__(self, var1, var2):
      print ("Calling parent constructor")
      self.var1 = var1
      self.var2 = var2
      print(f"var1 = {self.var1} and var2 = {self.var2}")

# define child class
class Child(Parent): 
   def __init__(self, var1, var2, var3, var4):
      super().__init__(var1, var2)
      print("child constructor")
      self.var3 = var3
      self.var4 = var4
      print(f"var3 = {self.var3} and var4 = {self.var4}")

c = Child(1, 2, 3, 4)

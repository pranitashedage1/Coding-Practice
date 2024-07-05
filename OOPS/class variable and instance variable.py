'''
class variable and instance variable - 
'''
class Test:
    classVar = 0

    def __init__(self, value):
        self.instance_var = value
        local_val = 0
        print("loacl_Val = ", local_val)

    def testing(self):
        self.testing_var = 50

t1 = Test(1)
t2 = Test(2)

# Accessing class variables
print("1 class_Variable - t1 = ", t1.classVar)
print("1 class_Variable - t2 = ", t2.classVar)

# Accessing instance variables
print('1 instance varibales t1 = ', t1.instance_var)
print('1 instance_variable  t2= ', t2.instance_var)

# modifying class variable
Test.classVar = 10
# t1.classVar = 34
print("2 class_Variable - t1 = ", t1.classVar)
print("2 class_Variable - t2 = ", t2.classVar)

# modifying instance variable
t1.instance_var = 20
print('2 instance varibales t1 = ', t1.instance_var)
print('2 instance_variable  t2= ', t2.instance_var)

print("testing = ", Test(60))
print('3 instance varibales = ', t1.instance_var)
print('3 instance_variable = ', t2.instance_var)

Test.instance_var = 100
print('trial1 - ', Test.instance_var)
print('4 instance varibales = ', t1.instance_var)
print('4 instance_variable = ', t2.instance_var)

t1.testing_var = 200
# Test(3).testing()
# print('trial2 - ', Test(4).testing_var)

# priting instance variable inside testing method- 

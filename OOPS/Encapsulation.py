'''
Encpauslation - Data members of class are available for processing to functions defined within class only.
'''

class Test:
    def __init__(self):
        self.__max_price = 20
    
    def sell(self):
       print(f"selling price {self.__max_price}")

t1 = Test()
t1.sell()
t1.__max_price = 300
print("data1 = ", t1.__max_price)
t1.sell()

# print("data1 = ", t1.data1)
# t1.data1 = 100
# print("data1 = ", t1.data1)

# print("data1 = ", t1.__data2)
# t1.__data2 = 200
# print("data1 = ", t1.__data2)

# class Desktop:
#    def __init__(self):
#       self.__max_price = 25000

#    def sell(self):
#       return f"Selling Price: {self.__max_price}"

#    def set_max_price(self, price):
#       if price > self.__max_price:
#          self.__max_price = price

# # Object
# desktopObj = Desktop()
# # print(desktopObj.sell()) 

# # modifying the price directly
# desktopObj.__max_price = 35000
# print(desktopObj.__max_price)
# # print(desktopObj.sell()) 

# # modifying the price using setter function
# desktopObj.set_max_price(35000)
# # print(desktopObj.sell())        
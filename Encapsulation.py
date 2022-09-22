###################### Encapsulation #####################################33

##### demonstrate protected members #######

class Base:
	def __init__(self):

		# Protected member
		self._a = 2

class Derived(Base):
	def __init__(self):

		Base.__init__(self)
		print("Calling protected member of base class: ",
			self._a)

		self._a = 3
		print("Calling modified protected member outside class: ",
			self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)


##### demonstrate private members ######

class Base:
	def __init__(self):
		self.a = "am private A"
		self.__c = "Am Private C"

# Creating a derived class
class Derived(Base):
	def __init__(self):

		
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)
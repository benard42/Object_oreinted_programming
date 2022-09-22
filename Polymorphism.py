class Manchester_United():
	def Location(self):
		print("The location of machester united is manchester North West England.")

	def Get_Best_Player(self):
		print("The best player in manchester is Jose Diogo Dalot Teixeira.")

	def type(self):
		print("Jose Diogo Dalot Teixeira is a left back defender.")

class Arsenal():
	def Location(self):
		print("The location of Arsenal is London Borough of Islington, London, United Kingdom.")

	def Get_Best_Player(self):
		print("The best player in Arsenal is  Bukayo Saka.")

	def type(self):
		print(" Bukayo Saka is a Forward.")

obj_manu = Manchester_United()
obj_Arsenal = Arsenal()
for Club in (obj_manu, obj_Arsenal):
	Club.Location()
	Club.Get_Best_Player()
	Club.type()

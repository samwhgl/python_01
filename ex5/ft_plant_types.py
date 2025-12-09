# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 17:28:38 by shaegels          #+#    #+#              #
#    Updated: 2025/12/08 18:14:02 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# ft_plant_types.py

class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age

	def get_info(self):
		return f"{self.name}: {self.height}cm, {self.age} days"

class Flower(Plant):
	def __init__(self, name, height, age, color):
		super().__init__(name, height, age)
		self.color = color

	def bloom(self):
		print(f"{self.name} is blooming beautifully!")

	def get_info(self):
		return f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color"

class Tree(Plant):
	def __init__(self, name, height, age, trunk_diameter):
		super().__init__(name, height, age)
		self.trunk_diameter = trunk_diameter

	def produce_shade(self):
		shade = self.height + self.trunk_diameter
		print(f"{self.name} provides {shade} square meters of shade")

	def get_info(self):
		return f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter"

class Vegetable(Plant):
	def __init__(self, name, height, age, nutritional_value, harvest_season):
		super().__init__(name, height, age)
		self.nutritional_value = nutritional_value
		self.harvest_season = harvest_season

	def get_info(self):
		return f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest"
	def get_nutritional_values(self):
		return f"{self.name} is rich in {self.nutritional_value}"


if __name__ == "__main__":
	rose = Flower("Rose", 25, 30, "red")
	oak = Tree("Oak", 500, 1825, 50)
	tomato = Vegetable("Tomato", 80, 90, "vitamin C", "summer")

	print("=== Garden Plant Types ===\n")
	print(rose.get_info())
	rose.bloom()
	print(oak.get_info())
	oak.produce_shade()
	print(tomato.get_info())
	print(tomato.get_nutritional_values())

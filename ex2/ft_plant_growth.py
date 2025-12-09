# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 15:57:55 by shaegels          #+#    #+#              #
#    Updated: 2025/12/08 16:14:40 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# ft_plant_growth.py

class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.age = age
		self.height = height

	def grow(self, cm):
		self.height += cm

	def age_plant(self, days):
		self.age += days

	def get_info(self):
		return f"{self.name}: {self.height}cm, {self.age} days old"

if __name__ == "__main__":
	rose = Plant("Rose", 25, 30)
	sunflower = Plant("Sunflower", 80, 45)
	cactus = Plant("Cactus", 15, 120)

	garden_plants = [rose, sunflower, cactus]

	print("=== Day 1 ===")
	for plant in garden_plants:
		print(plant.get_info())

	print("\n=== Day 7===")
	growth_week = {"Rose": 6, "Sunflower": 10, "Cactus": 1}
	for plant in garden_plants:
		plant.grow(growth_week[plant.name])
		plant.age_plant(6)
		print(plant.get_info())
		print(f"Growth this week: +{growth_week[plant.name]}cm")

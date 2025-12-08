# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 15:45:25 by shaegels          #+#    #+#              #
#    Updated: 2025/12/08 15:53:54 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# ft_garden_data.py

class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.age = age
		self.height = height

	def __str__(self):
		return f"{self.name}: {self.height}cm, {self.age} days old"

if __name__ == "__main__":
	rose = Plant("Rose", 25, 30)
	sunflower = Plant("Sunflower", 80, 45)
	cactus = Plant("Cactus", 15, 120)

	garden_plants = [rose, sunflower, cactus]

	print("== Garden Plant Registry ==")
	for plant in garden_plants:
		print(plant)

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 16:20:12 by shaegels          #+#    #+#              #
#    Updated: 2025/12/08 16:32:08 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# ft_plant_factory.py

class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age

	def __str__(self):
		return f"{self.name} ({self.height}cm, {self.age} days)"

if __name__ == "__main__":
	plant_data = [
		("Rose", 25, 30),
		("Oak", 200, 365),
		("Cactus", 5, 90),
		("Sunflower", 80, 45),
		("Fern", 15, 120)
	]

	plants = [Plant(name, height, age) for name, height, age in plant_data]

	print("=== Plant Factory Output ===")
	for plant in plants:
		print(f"Created: {plant}")
	print(f"Total plants created: {len(plants)}")

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 16:33:31 by shaegels          #+#    #+#              #
#    Updated: 2025/12/08 17:27:35 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# ft_garden_security.py

class SecurePlant:
	def __init__(self, name, height, age):
		self.name = name
		self.age = 0
		self.height = 0
		print(f"Plant created: {self.name}")
		self.set_height(height)
		self.set_age(age)

	def set_height(self, height):
		if height < 0:
			print(f"Invalid operation attempted: height {height}cm [REJECTED]")
			print("Security: Negative height rejected")
		else:
			self._height = height
			print(f"Height updated: {self._height}cm [OK]")

	def set_age(self, age):
		if age < 0:
			print(f"Invalid operation attempted: age {age} days [REJECTED]")
			print("Security: Negative age rejected")
		else:
			self._age = age
			print(f"Age updated: {self._age} days [OK]")

	def get_height(self):
		return self._height

	def get_age(self):
		return self._age

	def get_info(self):
		return f"{self.name} ({self._height}cm, {self.age} days)"

if __name__ == "__main__":
	print("=== Garden Security System ===")
	rose = SecurePlant("Rose", 25, 35)
	rose.set_height(-5)
	rose.set_age(-10)
	rose.set_height(30)
	rose.set_age(35)
	print("Current plants:", rose.get_info())

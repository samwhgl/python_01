# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 18:42:07 by shaegels          #+#    #+#              #
#    Updated: 2025/12/09 15:59:06 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name, height):
		self.name = name
		self.height = height

	def grow(self):
		self.height += 1
		print(f"{self.name} grew 1cm")

	def __str__(self):
		return f"{self.name}: {self.height}cm"

class FloweringPlant(Plant):
	def __init__(self, name, height, color, blooming=True):
		super().__init__(name, height)
		self.color = color
		self.blooming = blooming

	def __str__(self):
		state = "(blooming)" if self.blooming else "(not blooming)"
		return f"{self.name}: {self.height}cm, {self.color} flowers {state}"

class PrizeFlower(FloweringPlant):
	def __init__(self, name, height, color, price, blooming=True):
		super().__init__(name, height, color, blooming)
		self.price = price

	def __str__(self):
		base = super().__str__()
		return f"{base}, Prize points: {self.price}"

class Garden:
	def __init__(self, owner):
		self.owner = owner
		self.plants = []
		self.added = 0
		self.total_growth = 0

	def add_plant(self, plant):
		self.plants.append(plant)
		self.added += 1
		print(f"Added {plant.name} to {self.owner}'s garden")

	def grow_all(self):
		print(f"{self.owner} is helping all plants grow...")
		for plant in self.plants:
			plant.grow()
			self.total_growth += 1

	def recap(self):
		print(f"=== {self.owner}'s Garden Report ===")
		print("Plants in garden:")
		for plant in self.plants:
			print(f"- {plant}")

class GardenManager:
	total_managers = 0
	def __init__(self):
		self.gardens = []
		GardenManager.total_managers += 1

	class GardenStats:
		def __init__(self, garden):
			self.garden = garden

		def type_summary(self):
			regular = sum(isinstance(plant, Plant) and not isinstance(plant, FloweringPlant) for plant in self.garden.plants)
			flowering = sum(isinstance(plant, FloweringPlant) and not isinstance(plant, PrizeFlower) for plant in self.garden.plants)
			prize = sum(isinstance(plant, PrizeFlower) for plant in self.garden.plants)
			return regular, flowering, prize

		def height_check(self):
			return all(plant.height > 0 for plant in self.garden.plants)

	def add_garden(self, garden):
		self.gardens.append(garden)

	@staticmethod
	def score_garden(garden):
		score = sum(plant.height for plant in garden.plants)
		score += sum(plant.price for plant in garden.plants if isinstance(plant, PrizeFlower))
		return score

	@classmethod
	def create_garden_network(cls):
		return cls()

	def report(self):
		for garden in self.gardens:
			stats = self.GardenStats(garden)
			garden.recap()
			reg, flow, prize = stats.type_summary()
			print("\n")
			print(f"Plants added: {garden.added}, Total growth: {garden.total_growth}cm")
			print(f"Plant types: {reg} regular, {flow} flowering, {prize} prize flowers")
			print("\n")
			print(f"Height validation test: {stats.height_check()}")

if __name__ == "__main__":
	print("=== Garden Management System Demo ===\n")
	manager = GardenManager()
	alice = Garden("Alice")
	manager.add_garden(alice)

	alice.add_plant(Plant("Oak Tree", 100))
	alice.add_plant(FloweringPlant("Rose", 25, "red"))
	alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
	print("\n")

	alice.grow_all()
	print("\n")
	manager.report()
	bob = Garden("Bob")
	manager.add_garden(bob)
	bob.add_plant(Plant("Fern", 90))
	bob.add_plant(PrizeFlower("Orchid", 2, "white", 0))
	scores = {g.owner: GardenManager.score_garden(g) for g in manager.gardens}
	print(f"Garden scores - Alice: {scores['Alice']}, Bob: {scores['Bob']}")
	print(f"Total gardens managed: {len(manager.gardens)}")

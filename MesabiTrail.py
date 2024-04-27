import tkinter as tk
from tkinter import messagebox
from tkinter import Tk, Label, PhotoImage
import random

class OregonTrail:
	def __init__(self):
		self.window = tk.Tk()
		self.window.title("The Mesabi Trail")
		self.window.minsize(512, 512)
		# Load an image
		self.bg_image = PhotoImage(file="x2.png")
		# Create a label with the image as the background
		self.bg_label = Label(self.window, image=self.bg_image)
		# Position the label to cover the entire window
		self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
		self.miles = 0
		self.health = 100
		self.food = 1000
		self.water = 500
		self.money = 1500
		self.party_size = 5
		self.wagon_speed = 10

		self.label_miles = tk.Label(self.window, text="Miles Traveled: 0 of 132")
		self.label_miles.pack()
		self.label_health = tk.Label(self.window, text="Health: 100")
		self.label_health.pack()
		self.label_food = tk.Label(self.window, text="Cannabis: 1000 grams")
		self.label_food.pack()
		self.label_water = tk.Label(self.window, text="Water: 500 gallons")
		self.label_water.pack()
		self.label_money = tk.Label(self.window, text="Money: 1500 dollars")
		self.label_money.pack()
		self.lable_distance_traveled = tk.Label(self.window, text="distance traveled: 0 miles")
		self.lable_distance_traveled
		self.button_travel = tk.Button(self.window, text="Travel", command=self.travel)
		self.button_travel.pack()
		self.button_rest = tk.Button(self.window, text="Rest", command=self.rest)
		self.button_rest.pack()
		self.button_shop = tk.Button(self.window, text="Shop", command=self.shop)
		self.button_shop.pack()

	def travel(self):
		distance_traveled = random.randint(1, 10)
		self.food -= 5 * self.party_size
		self.miles = self.miles + distance_traveled
		self.water -= 3 * self.party_size
		self.health -= random.randint(1, 5)
		self.label_miles['text'] = f"Miles Traveled: {self.miles} of 132"
		self.label_health['text'] = f"Health: {self.health}"
		self.label_food['text'] = f"Cannabis: {self.food} grams"
		self.label_water['text'] = f"Water: {self.water} gallons"
		messagebox.showinfo("Travel", f"You traveled {distance_traveled} miles.")

	def rest(self):
		self.health += 10
		self.label_health['text'] = f"Health: {self.health}"
		messagebox.showinfo("Rest", "You rested and gained 10 health points.")

	def shop(self):
		self.window_shop = tk.Toplevel(self.window)
		self.label_shop_money = tk.Label(self.window_shop, text=f"Money: {self.money} dollars")
		self.label_shop_money.pack()
		self.button_shop_food = tk.Button(self.window_shop, text="Buy Cannabis", command=self.buy_food)
		self.button_shop_food.pack()
		self.button_shop_water = tk.Button(self.window_shop, text="Buy Water", command=self.buy_water)
		self.button_shop_water.pack()

	def buy_food(self):
		if self.money >= 50:
			self.food += 100
			self.money -= 50
			self.label_food['text'] = f"Cannabis: {self.food} grams"
			self.label_shop_money['text'] = f"Money: {self.money} dollars"
			messagebox.showinfo("Shop", "You bought 100 grams of cannabis for 50 dollars.")
		else:
			messagebox.showinfo("Shop", "You don't have enough money to buy weed")

	def buy_water(self):
		if self.money >= 25:
			self.water += 50
			self.money -= 25
			self.label_water['text'] = f"Water: {self.water} gallons"
			self.label_shop_money['text'] = f"Money: {self.money} dollars"
			messagebox.showinfo("Shop", "You bought 50 gallons of water for 25 dollars.")
		else:
			messagebox.showinfo("Shop", "You don't have enough money to buy water.")

	def run(self):
		self.window.mainloop()

if __name__ == "__main__":
	game = OregonTrail()
	game.run()

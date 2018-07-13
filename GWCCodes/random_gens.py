from random import *
apps = ["Quesadillas", "Mozzarella Sticks", "Chips", "Tacos"]
mains = ["Pasta", "Chicken", "Soup", "Rice and Beans"]
desserts = ["Cake", "Ice Cream", "Tiramisu", "Creme Brulee"]

rand_apps = randint(0,len(apps)-1)
rand_mains = randint(0,len(mains)-1)
rand_desserts = randint(0,len(desserts)-1)
print("Random app: ", apps[rand_apps])
print("Random main: ", mains[rand_mains])
print("Random dessert: ", desserts[rand_desserts])

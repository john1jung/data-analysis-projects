food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_split = food.split(',')
food_split.sort()
print(food_split)

equipment_split = equipment.split(',')
equipment_split.sort()
print(equipment_split)

pets_split = pets.split(',')
pets_split.sort()
print(pets_split)

sleep_aids_split = sleep_aids.split(',')
sleep_aids_split.sort()
print(sleep_aids_split)

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.

cargo_hold = []


# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.



# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.



# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”

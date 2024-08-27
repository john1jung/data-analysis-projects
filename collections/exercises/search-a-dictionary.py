flavors = {
  'chocolate' : 0.35,
  'vanilla' : 0.35,
  'strawberry' : 0.42,
  'cookies and cream' : 0.45,
  'mint chocolate chip' : 0.42,
  'fudge chunk' : 0.45,
  'saffron' : 2.25,
  'garlic' : 0.05
}

## Set a variable called choice to the flavor you want to search for.
choice = 'mint chocolate chip'

## Use an if statement to check if choice is in the flavors dictionary.
if choice in flavors:
    
## If it is, set another variable called cost to the value associated with choice.
  cost = flavors[choice]
## If it isn’t, set cost to 0.
else:
  cost = 0
## Print the cost.
print('For', choice, 'the cost is', cost)

### Search a Dictionary Part 2:

## Initialize two variables: highest_cost to 0 and fanciest to an empty string.
highest_cost = 0
fanciest = ''
## Loop through the flavors dictionary using a for loop.
for flavor in flavors:
## For each flavor, check if its price is higher than highest_cost.
  if flavors[flavor] > highest_cost:
## If it is, update fanciest to this flavor and highest_cost to its price.
    fanciest = flavor
    highest_cost = flavors[flavor]
## After the loop, print the most expensive flavor.
print('The fanciest flavor is', fanciest, 'and it cost', highest_cost )
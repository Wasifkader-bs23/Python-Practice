from re import M


my_pizza=['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
friend_pizza=my_pizza[:]
my_pizza.append("pineapple")
friend_pizza.append("apple")
print("My favorite pizzas are:")
for x in my_pizza:
    print("\t\t\t",x)
print("\n\nMy friend's favorite pizzas are:")
for y in friend_pizza:
    print("\t\t\t\t",y)
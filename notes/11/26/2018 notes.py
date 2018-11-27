#11/26/2018 notes
shopping_list = ["whole milk","pc","eggs","trash xbox One","ps4"]
print(shopping_list)
print(shopping_list[0])
print("The second thing is the list is %s" % shopping_list[1])
print("The length of the list is %s" % len(shopping_list))


#changing elements is a list
shopping_list[0] = "2% milk"
print(shopping_list)

print(shopping_list[0])
# looping through list
for item in shopping_list:
    print(item)

#New list
new_list = ["eggs", "cheese", "oranges", "Raspberries"]
print(new_list)
new_list[2] = "apples"
print("The last thing in the list is %s" % new_list[len(new_list) - 1])
print(new_list)

# setting part of a list
print(new_list[1:3])
print(new_list[1:4])
print(new_list[1:])        #this goes all the way to the end no matter what and you dont have to put the number
print(new_list[:2])

holiday_list = []    #Always use square brackets to indicate a list
holiday_list.append("tacos")
holiday_list.append("bumblebee")
holiday_list.append("Red dead Redemption 2")
print(holiday_list)

#notice this is object.method(parameters)"

#Removing things from the a list
holiday_list.remove("tacos")
print(holiday_list)
#tacos
#Bumblebee
#redDead Redemption 2
"""
1Make a new list with 3 items
add a 4th item to the list
3 remove one of the first three items from the list
"""
christmass_list = []    #Always use square brackets to indicate a list
christmass_list.append("Black ops 4")
christmass_list.append("Gaming pc")
christmass_list.append("SoccerBall")                                  #Needs work
christmass_list.append("Chicken nuggets")
christmass_list.remove("Gaming pc")
print(christmass_list)
christmass_list.pop(0)      # Removes the item in index 0
print(christmass_list)


#tuple
brands = ("apple", "samsung","HTC") # notice the parentheseses

colors = ('blue','cyan','green','red','orange','purple','pink','teal','gold','magenta','turquoise')
print(len(colors))

# find the index
print(colors.index("gold"))

# changing things into a list
string1 = "turquoise"
list1 = list(string1)                          # help for the the project hang man
print(list1)


for character in list1:
    if character == "u":
        # replace with a *
    current_index = list1.index(character)
    list.pop(current_index)
    list.insert(current_index, "*")

#Change list into strings
print("".join(list1))
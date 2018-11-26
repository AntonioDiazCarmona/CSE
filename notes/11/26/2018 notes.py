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


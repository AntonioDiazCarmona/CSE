import random
words =["tomatoes","foodmax","fortnite","chicken","elephant","noodle","pepperoni","computer","pycharm","triangle",]
the_word = random.choice(words)
print(the_word)
letters =["a","b","c","d","e","f","g","h","i","j","k","l","m","o","p""q","r","s","t","u","v","w","x","y","z"]
letter = input("")
if letter in the_word:
    print(letter)

for character in list1:
    if character == "u":
        # replace with a *
        currrent_index = list1.index(character)
        list1.pop(currrent_index)
        list1.insert(currrent_index, "*")















# string1 = "turquoise"
# list1 = list(string1)
# print(list1)

# for character in the_word:
#     if character == "u":
#         # replace with a *
#         currrent_index = the_word.index(character)
#         the_word.pop(currrent_index)
#         the_word.insert(currrent_index, "*")

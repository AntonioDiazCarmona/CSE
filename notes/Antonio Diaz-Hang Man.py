import random
words =["tomatoes","foodmax","fortnite","chicken","elephant","noodle","pepperoni","computer","pycharm","triangle",]
the_word = random.choice(words)
print(the_word)
letters =["a","b","c","d","e","f","g","h","i","j","k","l","m","o","p""q","r","s","t","u","v","w","x","y","z"]
letter = input("")
if letter in the_word:
    print(letter)
string1 = the_word
list1 = list(string1)
print(list1)

for character in list1:
    if character == the_word:

        currrent_index = list1.index(character)
        list1.pop(currrent_index)
        list1.insert(currrent_index, "_")




the_word=["_"]
item_to_replace =("_")
replacement_value =[]
 indices_to_replace = [i for i,x in enumerate(a) if x==item_to_replace]
indices_to_replace
[0, 5, 10]
for i in indices_to_replace:
  the_word[i] = replacement_value



# output['_','_','_','_','_']
# # for i in range(for len(the_word))
# # ['m','a','n','g','o']
# #     output=["m"
# #         output['_','_','_','_','_']
# list.append letters_used
#
#
# # the_word len['_']
# #




# string1 = "turquoise"
# list1 = list(string1)
# print(list1)

# for character in the_word:
#     if character == "u":
#         # replace with a *
#         currrent_index = the_word.index(character)
#         the_word.pop(currrent_index)
#         the_word.insert(currrent_index, "*")

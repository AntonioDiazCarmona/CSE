
            import random

        words = ["tomatoes", "foodmax", "fortnite", "chicken", "elephant", "noodle", "pepperoni", "computer",
                     "pycharm", "triangle", ]
        the_word = random.choice(words)
        print(the_word)
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p""q", "r", "s", "t", "u",
                       "v", "w", "x", "y", "z"]
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

            output = ['_']
            for i in range(for len(the_word))
            ['_']
            output = letters
            output['_', '_', '_', '_', '_']
            letters_used.append

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

            string1 = the_word
            list1 = list(string1)
            print(list1)

            for character in list1:
                if character == letters:
                    # replace with a *
                    currrent_index = list1.index(character)
                    list1.pop(currrent_index)
                    list1.insert(currrent_index, "*")


print("you have used these letters", + letters_used)

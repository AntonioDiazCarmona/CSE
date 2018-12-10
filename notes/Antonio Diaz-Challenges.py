def challengeE1(firstname,lastname):
    print ("Your name is   " + lastname + " " + firstname)
challengeE1("John", "Doe")

def challgengeE2(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

challgengeE2(57)


def challengeE3(base, height):
    area = base * height / 2
    print("area = %d" % area)

challengeE3(4, 6)

def challengeE4(number):
    if number > 0:
        print("Positive number")
    elif number == 0:
        print("Zero")
    else:
        print("Negative number")
challengeE4(0)



def challengeE9(str):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if str in vowel:
        print("Letter is vowel")
    else:
        print("Letter is consonant")

challengeE9("a")

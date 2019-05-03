import csv


def sixteen(num):
    if len(num) == 16:
        return True
    return False


def reverse_it(num):
    return num[::-1]


def change_to_int(num_list: list):
    for index in range(len(num_list)):
        num_list[index] = int(num_list[index])

    return num_list


def validate(num: str):
    if not sixteen(num):
        return False
    last_num = int(num[15])
    # this is basically like you said instead of doing :-1 this basically  taking off the last number
    num = num[:15]
    reverse_number = reverse_it(num)
    # Turn everything into a number
    list_version = list(reverse_number)
    number_list = change_to_int(list_version)  # change to a for loop
    print(number_list)
    added_numbers = 0
    for i in range(len(number_list)):
        # basically converting the the numbers position  into like an integer for example 4 would be index 0
        # this is the index
        # index 0 % 2 == -0
        # index 2 % 2 == 0
        #  etc etc
        # so these are the 'odd' digits
        # and we just do the formula on them
        if i % 2 == 0:
            # the i is basically the interger and == 0 is basically saying its odd because it starts at index 0
            # this is odd number
            number_list[i] *= 2
            # multiply by 2
            if number_list[i] > 9:
                # if they are bigger than 9
                # minus 9
                number_list[i] -= 9
                # add them
            # THIS must be the digits that are 1, 3, 5 etc
            # so we don't do anything but add them!
        added_numbers += number_list[i]
    # so our for loop is over
    # you need to use the last num, and this added_numbers
    # to do the 'final' step
    # add and check if mod 10 is 0

    return added_numbers % 10 == last_num


# print(validate("4556737586899855"))

with open("Book1.csv", 'r') as old_csv:
    with open("InvalidNums.csv", "w", newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")
        for row in reader:
            old_number = row[0]  # string
            if validate(old_number):
                writer.writerow(row)
        print("OK")

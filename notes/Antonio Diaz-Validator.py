import csv


def sixteen(num):
    if len(num) == 16:
        return True
    return False


def reverse_it(num):
    return num[::-1]
# list(int(d) for d in str(int(*)))

def change_to_int(num_list: list):
    for index in range(len(num_list)):
        num_list[index] = int(num_list[index])
    return num_list


def validate(num: str):
    if not sixteen(num):
        return False
    last_num = int(num[15])
    num = num[:15]
    reverse_number = reverse_it(num)

    # Turn everything into a number
    list_version = list(reverse_number)
    number_list = change_to_int(list_version)
    print(number_list)

    for index in range(list_version)
        list_version[index] *= 2


    if reverse_number > 9:
        reverse_number -= 9


        added_numbers = 0
        added_numbers += reverse_number

validate("4556737586899855")

# with open("Book1.csv", 'r') as old_csv:
#     with open("InvalidNums.csv", "w", newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Processing...")
#         for row in reader:
#             old_number = row[0]  # string
#             if validate(old_number):
#                 writer.writerow(row)
#         print("OK")















        #
        # def validate(num: str):
        #     if first_num_odd(num) and second_num_even(num):
        #         return True
        #     return False
        #
        # def reverse(num: str):
        #     print(num)
        #     print(num[::-1])  # how to reverse a number
        #
        # reverse("5820859753077330")
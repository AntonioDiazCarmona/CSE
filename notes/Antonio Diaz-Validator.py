import csv


def sixteen(num):
    if len(num) == 16:
        return True
    return False


def validate(num: str):
    if not sixteen(num):
        return False
    last_num =




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
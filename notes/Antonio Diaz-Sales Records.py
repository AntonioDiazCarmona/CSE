import csv


with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")
    fruit_profit = 0
    clothes_profit = 0
    meat_profit = 0
    Beverages_profit = 0
    Office_Supplies_profit = 0
    Cosmetics_profit = 0
    Snacks_profit = 0
    Personal_care_profit = 0
    Household_profit = 0
    Vegetables_profit = 0
    Baby_Food_profit = 0
    Cereal_profit = 0
    for row in reader:
        if row[0] == 'Region':
            continue
        Total_profit = float(row[13])
        Total_cost = row[12]  # string
        Total_revenue = row[11]
        Item_selling = row[2]
        # print("you are selling", Item_selling)
        # print("Your total profit is", Total_profit)
        # print("Your total revenue is", Total_revenue)
        # print("Your total cost for all the items you bought is", Total_cost)
        if "Fruits" == Item_selling:
            # print("You are selling", Item_selling)
            # print("You total cost for buying fruits is", Total_cost)
            # print("your total revenue is ", Total_revenue)
            # print("You made a profit of", Total_profit)

            fruit_profit += Total_profit
        if "Clothes" == Item_selling:
            clothes_profit += Total_profit
        if "Meat" == Item_selling:
            meat_profit += Total_profit
        if "Beverages" == Item_selling:
            Beverages_profit += Total_profit
        if "Office Supplies" == Item_selling:
            Office_Supplies_profit += Total_profit
        if "Cosmetics" == Item_selling:
            Cosmetics_profit += Total_profit
        if "Snacks" == Item_selling:
            Snacks_profit += Total_profit
        if "Personal Care" == Item_selling:
            Snacks_profit += Total_profit
        if "Household" == Item_selling:
            Snacks_profit += Total_profit
        if "Vegetables" == Item_selling:
            Snacks_profit += Total_profit
        if "Baby Food" == Item_selling:
            Snacks_profit += Total_profit
        if "Cereal" == Item_selling:
            Snacks_profit += Total_profit

    print("Your total fruit profit added is", round(fruit_profit, 2))
    print("Your total clothes profit added is", round(clothes_profit, 2))
    print("Your total meat profit added is", round(meat_profit, 2))
    print("Your total beverages profit added is", round(Beverages_profit, 2))
    print("Your total Office Supplies profit added is", round(Office_Supplies_profit, 2))
    print("Your total Cosmetics profit added is", round(Cosmetics_profit, 2))
    print("Your total Snacks profit added is", round(Snacks_profit, 2))
    print("your total personal care profit added is", round(Personal_care_profit, 2))  # here
    print("your total household profit added is", round(Household_profit, 2))
    print("Your total vegetables profit added is ", round(Vegetables_profit, 2))
    print("Your total baby food profit added is ", round(Baby_Food_profit, 2))
    print("Your total cereal profit added is ", round(Cereal_profit))
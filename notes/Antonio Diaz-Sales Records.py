import csv


with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")
    for row in reader:
        Total_profit = float(row[13])
        Total_cost = row[12]  # string
        Total_revenue = row[11]
        Item_selling = row[2]
        # print("you are selling", Item_selling)
        # print("Your total profit is", Total_profit)
        # print("Your total revenue is", Total_revenue)
        # print("Your total cost for all the items you bought is", Total_cost)
        if "Fruits" == Item_selling:
            print("You are selling", Item_selling)
            print("You total cost for buying fruits is", Total_cost)
            print("your total revenue is ", Total_revenue)
            print("You made a profit of", Total_profit)
            fruit_profit = 0
            fruit_profit += Total_profit
            print("Your total fruit profit added is", fruit_profit)

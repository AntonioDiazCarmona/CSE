import csv


with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")

    for row in reader:
        Total_profit = row[13]
        Total_cost = row[12]  # string
        Total_revenue = row[11]
        Item_selling = row[2]
        print("you are selling", Item_selling)
        print("Your total profit is", Total_profit)
        print("Your total revenue is", Total_revenue)
        print("Your total cost for all the items you bought is", Total_cost)

   if "Fruits" in row[2]:
       print("you total cost for buying fruits is", Total_cost)
       Total_revenue -= Total_cost
       print("print you made a profit of", Total_profit)

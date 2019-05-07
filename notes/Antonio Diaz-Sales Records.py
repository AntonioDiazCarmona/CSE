with open("Sales Records.csv", 'r') as old_csv:
    with open("MySaleRecords.csv", "w", newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]  # string
            if validate(old_number):
                writer.writerow(row)
        print("OK")

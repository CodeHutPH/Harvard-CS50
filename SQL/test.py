import csv  # Import the csv module for reading and writing CSV files

with open("./csv/fav.csv", "r") as file:  # Open the CSV file named "fav.csv" in read mode ("r")
    reader = csv.reader(file)  # Create a CSV reader object
    next(reader)  # Skip the header row, moving the file cursor to the next row

    for row in reader:  # Iterate through each row in the CSV file
        print(row[1], row[5], row[8]) # Print specific columns from each row (columns 2, 6, and 9, considering zero-based indexing)

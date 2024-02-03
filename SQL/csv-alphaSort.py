import csv
from collections import Counter

def count_and_sort_5th(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            # Assuming CSV has a header, adjust the code if there is no header
            reader = csv.reader(csvfile)
            next(reader, None)  # Skip header
            
            # Use Counter to count values in the 5th column
            counts = Counter(row[4] for row in reader) #EDIT row[n] for ADJUSTMENTS
            
            # Print results in alphabetical order
            for entry in sorted(counts):
                print(f"{entry}: {counts[entry]}")
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Provide the path to your CSV file
file_path = "./csv/fav.csv"

# Call the function with the file path
count_and_sort_5th(file_path)
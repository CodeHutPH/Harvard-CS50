import csv
from collections import Counter

# Function to read CSV file, count values in the 5th column, and print sorted results
def count_and_sort_5th(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            # Assuming CSV has a header, adjust the code if there is no header
            reader = csv.reader(csvfile)
            
            # Skip header
            next(reader, None)
            
            # Use Counter to count values in the 5th column
            counts = Counter(row[5] for row in reader) #EDIT row[n] for ADJUSTMENTS
            
            # Print results in descending order of counts
            for entry, count in counts.most_common():
                print(f"{entry}: {count}")
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Provide the path to your CSV file
file_path = "./csv/fav.csv"

# Call the function with the file path
count_and_sort_5th(file_path)
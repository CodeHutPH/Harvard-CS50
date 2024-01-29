def get_average():
    # Get user input for the number of scores
    num_scores = int(input("Enter the number of scores: "))

    # Validate that the number of scores is positive
    while num_scores <= 0:
        print("Please enter a positive number.")
        num_scores = int(input("Enter the number of scores: "))

    # Initialize an empty list to store the scores
    scores = []

    # Loop to get input for each score
    for i in range(num_scores):
        score = float(input(f"Enter score #{i + 1}: "))
        scores.append(score)

    # Calculate the average
    average = sum(scores) / num_scores

    # Print the result
    print(f"The average of {num_scores} scores is: {average:.2f}")

# Call the function to calculate and print the average
get_average()

# Add a delay to keep the terminal open
input("Press Enter to exit...")

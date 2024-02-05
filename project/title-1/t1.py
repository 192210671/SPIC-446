import pandas as pd
import numpy as np

def calculate_mean_accuracy(csv_path, iterations=20):
    # Initialize an empty list to store accuracy values for each iteration
    accuracy_values = []

    for _ in range(iterations):
        # Load CSV data into a pandas DataFrame
        df = pd.read_csv(csv_path)

        # Assuming ProxyProcessingAccuracy and ModelAccuracy are columns in the CSV
        # Replace these column names with the actual column names in your CSV
        proxy_processing_accuracy = df['ProxyProcessingAccuracy']
        model_accuracy = df['ModelAccuracy']

        # Calculate mean accuracy for the current iteration
        mean_accuracy = np.mean([proxy_processing_accuracy, model_accuracy])

        # Append mean accuracy to the list
        accuracy_values.append(mean_accuracy)

    # Calculate the overall mean accuracy across all iterations
    overall_mean_accuracy = np.mean(accuracy_values)

    return overall_mean_accuracy, accuracy_values

# Replace 'your_dataset.csv' with the actual path to your CSV file
csv_path = 'your_dataset.csv'

# Set the number of iterations (default is 20)
iterations = 20

# Call the function to calculate mean accuracy
mean_accuracy, accuracy_values = calculate_mean_accuracy(csv_path, iterations)

# Print the results
print(f"Overall Mean Accuracy: {mean_accuracy}")
print("Mean Accuracy for Each Iteration:")
for i, acc in enumerate(accuracy_values, start=1):
    print(f"Iteration {i}: {acc}")

import pandas as pd
import numpy as np

# Create a sample DataFrame with NaN values
data = {'A': [1, 2, "", 4, 5],
        'B': [5,"", 7, 8, 9]}

df = pd.DataFrame(data)

# Calculate the mean of each column
mean_values = df.mean()

# Display the mean values
print("Mean values:")
print(mean_values)
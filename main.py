# CAP4770 - Data Mining
# Assignment 1
# Evon Troy Alexander

import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# We will load the Titanic dataset
df = pd.read_csv('titanic.csv')

# We will print the dataset
print(df.head())

# Count the number of rows in df
original_rows = len(df)

# Drop 'deck' from the DataFrame
df = df.drop(columns='deck')

# Drop rows with any missing values
df_dropped = df.dropna()

# Count the number of rows in df_dropped
shortened_rows = len(df_dropped)

# Subtract the number of rows in df_dropped from the original number of rows
removed_rows = original_rows - shortened_rows

# Print the number of observations/rows removed
print(f"The number of observations/rows removed is: {removed_rows}")

# Calculate the standard deviation and mean of 'fare' numeric feature
fare_std = df['fare'].std()
fare_mean = df['fare'].mean()

# Remove observations with 'fare' values greater than mean + 2 standard deviations
# or less than mean - 2 standard deviations

df_filtered = df.loc[(df['fare'] >= fare_mean - 2 * fare_std) & (df['fare'] <= fare_mean + 2 * fare_std)]

# Draw a histogram of fare feature before outliers
matplotlib.pyplot.hist(df['fare'], density=True, bins=30)
plt.title('Step 4. Fare before removing outliers')
plt.ylabel('Probability')
plt.xlabel('Fare')
plt.show()

# Step 4. Draw the boxplot of column 'fare' before removing outliers
df.boxplot(column=['fare'])
plt.title('Step 4. Fare before removing outliers')
plt.show()

# Step 4. Draw a histogram of fare feature after removing outliers
matplotlib.pyplot.hist(df_filtered['fare'], density=True, bins=30)
plt.title('Step 4. Fare after removing outliers')
plt.ylabel('Probability')
plt.xlabel('Fare')
plt.show()

# Step 4. Draw the boxplot of column 'fare' after removing outliers
df_filtered.boxplot(column=['fare'])
plt.title('Step 4. Fare after removing outliers')
plt.show()

# Calculate the interquartile (IQR) range of 'age' and 'fare' features
age_quartile1 = df['age'].quantile(0.25)
age_quartile3 = df['age'].quantile(0.75)
age_iqr = age_quartile3 - age_quartile3

fare_quartile1 = df['fare'].quantile(0.25)
fare_quartile3 = df['fare'].quantile(0.75)
fare_iqr = fare_quartile3 - fare_quartile1

# Assign the upper and lower bounds of 'age' and 'fare' features
age_lower_bound = age_quartile1 - 1.5 * age_iqr
age_upper_bound = age_quartile3 + 1.5 * age_iqr

fare_upper_bound = fare_quartile3 + 1.5 * fare_iqr
fare_lower_bound = fare_quartile1 - 1.5 * fare_iqr

# Filter the DataFrame to remove observations with 'age' or 'fare' values greater than the upper bound
filtered_df = df.loc[
    (df['age'] >= age_lower_bound) & (df['age'] <= age_upper_bound) &
    (df['fare'] >= fare_lower_bound) & (df['fare'] <= fare_upper_bound)
    ]
# Step 5. Draw a histogram of age feature after removing outliers
matplotlib.pyplot.hist(filtered_df['age'], density=True, bins=30)
plt.title('Step 5. age after removing outliers')
plt.show()

# Step 5. Draw the boxplot of column 'age' after removing outliers
filtered_df.boxplot(column=['age'])
plt.title('Step 5. age after removing outliers')
plt.show()

# Step 5. Draw a histogram of fare feature after removing outliers
matplotlib.pyplot.hist(filtered_df['fare'], density=True, bins=30)
plt.title('Step 5. Fare after removing outliers')
plt.show()

# Step 5. Draw the boxplot of column 'fare' after removing outliers
filtered_df.boxplot(column=['fare'])
plt.title('Step 5. Fare after removing outliers')
plt.show()

# Titanic Dataset Analysis

## Overview
The Titanic dataset provides information about the passengers aboard the Titanic, which sank in the Atlantic Ocean in 1912. In this project, I analyze the dataset using Python and pandas library to perform data cleaning and exploratory data analysis.

## Steps

1. **Reading the Dataset**
    - Used pandas.DataFrame.read_csv function to read the Titanic dataset and stored it into a pandas.DataFrame variable.

2. **Removing Empty Cells**
    - Utilized pandas.DataFrame.dropna function to remove all empty cells in the dataset.
    - Calculated the number of removed observations/rows by comparing the lengths of the original and modified DataFrames.

3. **Alternative Data Cleaning**
    - Recognized the significant loss of data (approximately 80%) caused by dropping all empty cells.
    - Implemented an alternative approach: first removing the 'deck' column, and then dropping empty cells from the remaining columns.
    - Determined the number of observations lost in this step.

4. **Handling Extreme Fare Values**
    - Calculated the mean (μ) and standard deviation (σ) of the 'fare' numeric feature.
    - Removed observations with 'fare' values greater than μ + 3σ or less than μ - 3σ to eliminate extreme values.
    - Illustrated the changes using histograms and boxplots before and after removing extreme fare values.

5. **Filtering Outliers**
    - Defined outliers as values at least 1.5 times the interquartile range above the third quartile or below the first quartile.
    - Filtered out observations with outlier values in 'age' or 'fare' features.
    - Visualized the impact of outlier removal on histograms and boxplots, comparing with the results of step 4.

## Conclusion
This project provides insights into the Titanic dataset by employing various data cleaning techniques and exploratory data analysis methods. Through the outlined steps, we aim to prepare the data for further analysis while ensuring the integrity and reliability of the findings.

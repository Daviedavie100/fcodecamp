# Medical data visualizer

Cleaned, normalized the medical examination dataset and explored the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices using 2 charts.

## Project

Visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas libraries. 

1. Created a chart, which shows the counts of good and bad outcomes for the cholesterol, gluc, alco, active, and smoke variables for patients with cardio=1 and cardio=0 in different panels.

![image](https://user-images.githubusercontent.com/7541585/215342972-57fb21cb-8235-44ab-b13f-3fe8f3256ee0.png)

2. Created a correlation matrix using the dataset.

![image](https://user-images.githubusercontent.com/7541585/215343116-c2de7385-849a-4784-87af-7c2873921829.png)


## Dataset

The dataset values were collected during medical examinations.

File name: medical_examination.csv

## Data description

The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. 

## Objective

Using the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

## Tasks

### Added an overweight column to the data. 

- To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. 
- If that value is > 25 then the person is overweight. 
- Use the value 0 for NOT overweight and the value 1 for overweight.

### Normalized the data by making 0 always good and 1 always bad. 

- If the value of cholesterol or gluc is 1, make the value 0 and If the value is more than 1, make the value 1.
- Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot(). 
- The dataset is split by 'Cardio' so there is one chart for each cardio value. 

### Cleaned the data. 

Filter out the following patient segments that represent incorrect data:

- diastolic pressure is higher than systolic 
- height is less than the 2.5th percentile (Keep the correct data with `df['height'] >= df['height'].quantile(0.025))`
- height is more than the 97.5th percentile
- weight is less than the 2.5th percentile
- weight is more than the 97.5th percentile

### Created a correlation matrix using the dataset. 

- Plot the correlation matrix using seaborn's heatmap()
- Mask the upper triangle

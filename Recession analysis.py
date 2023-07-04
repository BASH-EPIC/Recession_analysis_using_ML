#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Recession data
data = pd.DataFrame({
    'Time Period': ['01/2020', '02/2020', '03/2020', '04/2020', '05/2020', '06/2020', '07/2020', '08/2020', '09/2020',
                    '10/2020', '11/2020', '12/2020', '01/2021', '02/2021', '03/2021', '04/2021', '05/2021', '06/2021',
                    '07/2021', '08/2021', '09/2021', '10/2021', '11/2021', '12/2021', '01/2022', '02/2022', '03/2022',
                    '04/2022', '05/2022', '06/2022', '07/2022', '08/2022', '09/2022', '10/2022', '11/2022', '12/2022'],
    'GDP Growth': [0.3, -0.5, -7, -20.9, 3.2, 9, 7.4, 2, 1.1, 0.6, -1.8, 1.8, -2.9, 0.7, 2.3, 3.1, 1.3, 1, -0.2, 0.9, 0.6,
                   0.1, 1, 0.1, 0.1, 0, 0.1, -0.2, 0.7, -0.9, 0.3, 0, -0.8, 0.5, 0.1, -0.5]
})

# Convert 'Time Period' column to datetime format
data['Time Period'] = pd.to_datetime(data['Time Period'])

# Rename the 'GDP Growth' column to 'GDP Growth Rate'
data.rename(columns={'GDP Growth': 'GDP Growth Rate'}, inplace=True)

# Calculate recession based on quarterly GDP growth rate
data['Recession'] = data['GDP Growth Rate'] < 0

# Save the DataFrame to a CSV file
data.to_csv('UK_monthly_gdp.csv', index=False)

# Calculate the correlation matrix
corr_matrix = data.corr()

# Generate the correlation chart
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Chart')
plt.show()

# Set the 'Time Period' column as the index
data.set_index('Time Period', inplace=True)

# Select specific time periods for comparison
periods_to_compare = ['01/2020', '04/2020', '07/2020', '10/2020', '01/2021', '04/2021', '07/2021', '10/2021', '01/2022']
selected_data = data.loc[periods_to_compare, 'GDP Growth Rate']

# Plot the comparison chart
plt.figure(figsize=(10, 6))
selected_data.plot(kind='bar')
plt.title('Comparison of GDP Growth Rate')
plt.xlabel('Time Period')
plt.ylabel('GDP Growth Rate')
plt.xticks
plt.show()

# Resample the data to quarterly frequency and calculate the mean
quarterly_data = data['GDP Growth Rate'].resample('Q').mean()

# Create a new DataFrame for quarterly data
quarterly_df = pd.DataFrame({'Time Period': quarterly_data.index, 'GDP Growth Rate (Quarterly)': quarterly_data})

# Reset the index of the quarterly DataFrame
quarterly_df.reset_index(drop=True, inplace=True)

# Save the quarterly data to a new CSV file
quarterly_df.to_csv('UK_quarterly_gdp.csv', index=False)






# In[5]:


quarterly_df


# In[8]:


# Recession data
data = pd.DataFrame({
    'Time Period': ['01/2020', '02/2020', '03/2020', '04/2020', '05/2020', '06/2020', '07/2020', '08/2020', '09/2020',
                    '10/2020', '11/2020', '12/2020', '01/2021', '02/2021', '03/2021', '04/2021', '05/2021', '06/2021',
                    '07/2021', '08/2021', '09/2021', '10/2021', '11/2021', '12/2021', '01/2022', '02/2022', '03/2022',
                    '04/2022', '05/2022', '06/2022', '07/2022', '08/2022', '09/2022', '10/2022', '11/2022', '12/2022'],
    'GDP Growth': [0.3, -0.5, -7, -20.9, 3.2, 9, 7.4, 2, 1.1, 0.6, -1.8, 1.8, -2.9, 0.7, 2.3, 3.1, 1.3, 1, -0.2, 0.9, 0.6,
                   0.1, 1, 0.1, 0.1, 0, 0.1, -0.2, 0.7, -0.9, 0.3, 0, -0.8, 0.5, 0.1, -0.5]
})

# Convert 'Time Period' column to datetime format
data['Time Period'] = pd.to_datetime(data['Time Period'])

# Calculate recession based on quarterly GDP growth
data['Recession'] = data['GDP Growth'] < 0

# Set the 'Time Period' column as the index
data.set_index('Time Period', inplace=True)

# Plot the GDP growth and recession data
plt.figure(figsize=(10, 6))
data['GDP Growth'].plot(label='GDP Growth')
plt.fill_between(data.index, 0, data['GDP Growth'], where=data['Recession'], color='red', alpha=0.3)
plt.title('GDP Growth and Recession Data')
plt.xlabel('Time Period')
plt.ylabel('GDP Growth')
plt.legend()
plt.xticks(rotation=45)
plt.show()


# In[13]:


# Calculate the duration of each recession period
recession_periods = []
start_date = None
for idx, row in data.iterrows():
    if row['Recession'] and start_date is None:
        start_date = idx
    elif not row['Recession'] and start_date is not None:
        recession_periods.append((start_date, idx))
        start_date = None

# Calculate the magnitude and duration of each recession
recession_severity = []
for period in recession_periods:
    start_date, end_date = period
    recession_duration = (end_date - start_date).days + 1
    recession_magnitude = data.loc[start_date:end_date, 'GDP Growth'].sum()
    recession_severity.append((start_date, end_date, recession_magnitude, recession_duration))

# Plot the recession severity
plt.figure(figsize=(10, 6))
severity_dates = [period[0] for period in recession_severity]
severity_durations = [period[3] for period in recession_severity]
plt.bar(severity_dates, severity_durations, color='red')
plt.title('Recession Severity')
plt.xlabel('Recession Start')
plt.ylabel('Duration (days)')
plt.xticks(rotation=45)
plt.show()


# In[ ]:





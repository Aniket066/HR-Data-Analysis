import pandas as pd
import numpy as np

#read the data
df = pd.read_csv("HR.csv")
df

#get information about the data
df.info()
print(df.isnull().sum())

#observe the unnececery columns if there are any multi value
print(df['EmployeeCount'].value_counts())
print(df['StandardHours'].value_counts())
print(df['Over18'].value_counts())

#drop them
df = df.drop(['EmployeeCount', 'StandardHours', 'Over18'], axis=1)

#Eliminate the dataset's NaN values.
df = df.dropna()

#Giving the columns new names.
df = df.rename(columns={'Attrition': 'Attrition_rate'})

# sanitizing specific columns.
df['BusinessTravel'] = df['BusinessTravel'].str.replace('Travel_', '')
df['Attrition_rate'] = df['Attrition_rate'].str.replace('Yes', '1')
df['Attrition_rate'] = df['Attrition_rate'].str.replace('No', '0')
df['Gender'] = df['Gender'].str.replace('Female', 'F')
df['Gender'] = df['Gender'].str.replace('Male', 'M')


#eliminate any duplicate employee no.
df = df.drop_duplicates(subset='EmployeeNumber', keep="first")

df.head(10)

# Save the dataframe to a CSV file
df.to_csv('HR_changed.csv', index=False)


"""
The primary data structures in pandas are implemented as two classes:
+DataFrame, which you can imagine as a relational data table, with rows and named columns.
+Series, which is a single column. A DataFrame contains one or more Series and a name for each Series.
"""


city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

pd.DataFrame({ 'City name': city_names, 'Population': population })

#Import data from CSV
california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/ml_universities/california_housing_train.csv", sep=",")
california_housing_dataframe.describe()
california_housing_dataframe.head() #Describe first few records of DataFrame
california_housing_dataframe.hist('housing_median_age') #Distribution of values in a column

#Accessing data
#like dict/list in python
cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
print type(cities['City name'])
cities['City name']

print type(cities['City name'][1])
cities['City name'][1]

print type(cities[0:2])
cities[0:2]

#Manipulate data
population / 1000

import numpy as np
np.log(population) #pandas Series can be used as arguments to most NumPy functions

population.apply(lambda val: val > 100000) #Like map function

cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92]) #add Series to an existing DataFrame
cities['Population density'] = cities['Population'] / cities['Area square miles']
cities


#Indexes
#(assigns an identifier value to each Series item or DataFrame row.)
city_names.index
cities.index

cities.reindex([2, 0, 1]) #reindex to manually reorder the rows

cities.reindex(np.random.permutation(cities.index))

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Numpy
# - Create an array with shape (4, 3) of: a. all zeros b. ones c. numbers from 0 to 11
# - Tabulate the following function: F(x)=2x^2+5, x∈[1,100] with step 1.
# - Tabulate the following function: F(x)=e^−x, x∈[−10,10] with step 1.

a = np.zeros((4, 3))
b = np.ones((4, 3))
c = np.arange(0, 12, 1)
c = np.reshape(c, newshape=(4, 3))

func1 = np.arange(1, 101, 1)
x = 2*(func1^2)+5
print(*x, sep='\n')

func2 = -(np.arange(-10, 11, 1))
y = np.exp(func2)
print(*y, sep='\n')

# Pandas
# - Import the dataset from this address and assign it to df variable.
# - Select only the Team, Yellow Cards and Red Cards columns.
# - How many teams participated in the Euro2012?
# - Filter teams that scored more than 6 goals

df = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv')
df[['Team', 'Yellow Cards', 'Red Cards']]
teams = df['Team'].nunique()
teams_scored_more_than_6_goals = df.loc[df['Goals'] > 6]

# DataViz
# Choose a dataset, you can use Seaborn example datasets. Create a cheat sheet for yourself containing all plot types discussed in the lecture.
# Provide the following info:
#   - Plot type
#   - Use cases (categorical data, distribution, etc.)
#   - Example on the dataset

tips = sns.load_dataset('tips')
#Plot type: histogram
#Use cases: data distribution
sns.histplot(data=tips, x="total_bill", hue="sex")

#Plot type: scatter plot
#Use cases: data relationships
sns.relplot(data = tips, y="day", x="total_bill", kind='strip')

#Plot type: regression plot
#Use cases: bivariate data relationship
sns.regplot(data=tips, x="total_bill", y="tip")

#Plot type: distribution plot
#Use cases: data comparison, statistics
sns.catplot(data = tips, x="day", y="total_bill", hue="smoker", kind="box")
sns.catplot(data = tips, x="total_bill", y="day", hue="sex", kind="violin")
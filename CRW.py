#The first line
import pandas as pd

#Creating data
#Object in panas: DataFrame and Series

#Creating a DataFrame
p = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(p)

print('----------------------------------')

#DataFrame not limited for a int values
d = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print(d)

print('----------------------------------')

#Index: Use to name the rows (Out of the dictionary)
f = pd.DataFrame({'Luis': ['Me gusta', 'No me gusta'],
                'Fernando': ['Me encanta', 'No me encanta']},
                index=['Opinion 1', 'Opinion 2'])
print(f)

print('----------------------------------')


#Creating a Series
s = pd.Series([1, 2, 3, 4, 5])
print(s)

print('----------------------------------')


#Compairson: Series is a list and the DataFrame is a table

u = pd.Series([30, 35, 45], index=['2015 Sales', '2026 Sales', '2017 Sales'], name='Product A')
print(u)
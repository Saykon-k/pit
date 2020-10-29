import pandas
df  = pandas.read_csv('hrdata.csv')
print(df)
print()
print()
df  = pandas.read_csv('hrdata.csv',index_col='name',parse_dates=['Hire Date'])
print(df)
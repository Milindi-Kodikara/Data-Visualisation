import pandas as pd
print("Keywords of Fun Palace")
#Dictionary of Lists
#data = {'Name': ['Tom', 'Mili', 'WomBOI', '\'Burt!', 'Squank'],
# 'Type': ['Peasant', 'Pug', 'Wombat', 'Machine Learning Bot', 'Chat Bot']}

#List of dictionaries
data = [{'Name': 'Tom', 'Type': 'Peasant', 'But really': 'Human', 'Rating in WomhB': 5},
        {'Name': 'Mili', 'Type': 'Pug', 'But really': 'Human', 'Rating in WomhB': 5},
        {'Name': 'WomBOI', 'Type': 'Wombat', 'Rating in WomhB': 4},
        {'Name': '\'Burt!', 'Type': 'Machine Learning Bot', 'Rating in WomhB': 3},
        {'Name': 'Squank', 'Type': 'Chat Bot', 'Rating in WomhB': 2.5}]
df = pd.DataFrame(data, index=['1', '2', '3', '4', '5'])
print(df)
print()
print("A glimpse to all our characters: ")
print(df['Name'])
print()

#Adding a new column of data
df['Feature'] = ['General', 'General', 'General', 'Fud', 'SquankApp']
print(df)
print()
#Selecting a row of data
print("Guess who uses the measuring unit WohmB everyday! This guuuyyy:")
print(df[2:3])
print()
print("If you want their full details in another way:")
print(df.iloc[2])
print()

print("The actual data in our data frame is:")
print(df.values)
print()

print("The mean value in WomhBs")
print(df.mean())
print()

print("Summary of statistical data:")
print(df.describe())
print()
#Iterating the dataframe coz why not
print("Details in a concise way:")
for row_index, row in df.iterrows():
        print(row)
        print()

#Check for any missed data
print("Missing data?!")
print(df['But really'].isnull())
print()

#Group data by ranking
print("Ranks!")
print(df.groupby('Rating in WomhB').groups)
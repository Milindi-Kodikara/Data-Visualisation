import pandas as pd
print("Keywords of Fun Palace")
#Dictionary of Lists
#data = {'Name': ['Tom', 'Mili', 'WomBOI', '\'Burt!', 'Squank'],
# 'Type': ['Peasant', 'Pug', 'Wombat', 'Machine Learning Bot', 'Chat Bot']}

#List of dictionaries
data = [{'Name': 'Tom', 'Type': 'Peasant', 'But really': 'Human'},
        {'Name': 'Mili', 'Type': 'Pug', 'But really': 'Human'},
        {'Name': 'WomBOI', 'Type': 'Wombat'},
        {'Name': '\'Burt!', 'Type': 'Machine Learning Bot'},
        {'Name': 'Squank', 'Type': 'Chat Bot'}]
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
print("Guess who uses the measuring unit WohmB everyday!")
print(df[2:3])
print()
print("If you want their full details in another way:")
print(df.iloc[2])

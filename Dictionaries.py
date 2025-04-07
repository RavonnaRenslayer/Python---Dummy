#Dictionaries

Birthday_Dictionary = {'Emily': 'January 1984', 'Maxine' : 'July 1985' ,
'Kelly' : 'May 1955' , 'Violet' : 'July 2008'}

# The most common way to create a dictionary is by utilizing curly brackets {}.

print (Birthday_Dictionary)


# In the dictionary above the name is the key, and the birth date is the value.

print (Birthday_Dictionary ['Maxine'])

# The value returned is "July 1985".


# Replace someone's birthday: 

Birthday_Dictionary ['Emily'] = 'March 1983'
print (Birthday_Dictionary)


# Add text in combination with the displaying Dictionary:

print ("Kelly's Birthday is: " + Birthday_Dictionary ['Kelly'])


# Add another birthday:

Birthday_Dictionary ['Madnus'] = 'March 2018'


#Delete a key from a dictionary:

del Birthday_Dictionary ['Kelly']

print(Birthday_Dictionary)

      

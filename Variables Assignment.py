B = "Let's do some math!"
print (B)

X = 10
print ("X = 10")
print ("X plus 5 equals:")
print (X + 5)

A = 5
print ("A = 5")
print ("A minus X equals:")
print (A - X)
print ("X times by A equals:")
print (X * A)
print ("X divided by A equals:")
print (X / A)
print ("Is X larger than A?:")
print (X > A)
print ("Is X less than A?:")
print (X < A)
print ("Are X and A equal?:")
print (X == A)

if X > A:
    print ("X (being 10) is larger than A (which is 5)")
           

name = 'JULIANA'
print (name)

print ("Now it is time to print JULIANA in all lower case letters: " + name.lower())

list_names = ['Juliana', 'Djair', 'Scarlett', 'Jaqueline']

print ("Here's the list we created: ")
print (list_names)

print ("Here's the third name from the list we wrote in all caps: " + list_names [2].upper())

date = "October/16th/2024"

print ("Here's the date we created: " + date)

split_date = date.split ('/')

print ("Here's the date we entered split apart: ")
print (split_date)

another_name = 'Vanessa'

print ("We chose the name; " + another_name)
print ("Here's " + another_name + " written with the cases swapped: " + another_name.swapcase ())

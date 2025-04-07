#Here I am creating restriction for a driving test application. If 18 the person is allowed to apply for test, if 17 the person cannot apply.

answer = "18"

if answer == "18":
    print ("You can apply for your driving test")

elif answer == "17":
    print ("You cannot apply for your driving test, due to age restriction")

else:
    print ("You must enter your age")
    

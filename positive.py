x = input("Please enter your list of numbers(seperated by ,):").split(",")
y =list( map(int,x))
for i in y:
    if  i > 0:
        print (i)
    

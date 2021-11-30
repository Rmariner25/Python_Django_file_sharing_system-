#To print palindrome of a number 
x=int(input("Enter number:"))
y=str(x)
u=len(y)
g=" "
for i in range(-1,-(u+1),-1): #string backward indexing from -1 to -n
    g=g+y[i] #string concatenation 
print(g)
    

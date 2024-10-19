x=int(input("Enter number:"))
y=int(input("Enter number:"))
z=int(input("Enter number:"))
if (x>y>z):
 print(x,y,z)
elif (y>x>z):
 print(y,x,z)
elif (y>z>x):
 print(y,z,x)
elif (z>y>x):
 print(z,y,x)
elif (z>x>y):
 print(z,x,y)
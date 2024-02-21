inputs=[]
n=eval(input("Numbers of items:"))
for i in range(1,n+1):
    value=input("Price of item:")
    inputs.append(value)
total=0
for num in inputs:
    total+=eval(num)
if total<=100:
    print("Total price for",n,"items is $",total,end="")
else:print("Total price for",n,"items is $",total*0.9,end="")
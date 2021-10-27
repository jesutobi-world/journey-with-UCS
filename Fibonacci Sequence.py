previous_variable=0
step=1
limit=int(input("Enter the limit of the sequence: "))
new_variable=0
print(new_variable)
count=0
while count <= limit-1:
    previous_variable=step
    step=new_variable
    new_variable=previous_variable+step
    print(new_variable)
    count=count+1
    



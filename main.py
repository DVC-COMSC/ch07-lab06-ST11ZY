
inputvalues = input('Enter all elements values: ')
numbers1 = inputvalues.split() 
numbers2=[]
y=0
x=len(numbers1)
for i in range(x):
	numbers1[i] = int(numbers1[i]) 

# The following line is the same as the for-loop
# numbers1 = list(map(int, numbers))

print ("The original list: ", numbers1)
# ******************************
# Make your Code
# ******************************
x=x-1
while x>=0:
	numbers2.insert(y,numbers1[x])
	x=x-1
	y=y+1
print("New list:", numbers2)
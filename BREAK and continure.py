# i = 0
# while i <= 10:
    
    if(i %2 == 0):
     i += 1
     continue

    print(i)
    i+=1


crickter=("sachin", "virat", "rohit","dhoni","jadeja")

for val in crickter:
    print(val)
    
crickter=("sachin", "virat", "rohit","dhoni","jadeja") 
for val in crickter:
    print(val)

else:
    print("end")
    
    
str= ("apanacollege")
for char in str:
    if(char == "o"):
        ("o found")
        break
    print(char)

else:
    print("end")


nums = [ 1, 4, 16, 25, 36, 49, 64, 81, 100]
for el in nums:
    print(el)


nums=( 1, 4, 16, 25, 36, 49, 64, 81, 100, 64)
x=100
i=0

for el in nums:
    if(el == x):
        print("number found at inedx:", i)
        break
    i += 1


for i in range(1,101):
    print(i)

for i in range(100,0, -1):
    print(i)


n=int(input("enter number"))
for i in range(1,11):
    print(n *i)



n=15

sum = 0
for i in range(10):

for i in range(1, n+1):
    sum += i
print("total sum",sum)
    

n=5
fact=1
i=1
while i <= n:
    fact *= i
    i +=2
    print("factorial =",fact)
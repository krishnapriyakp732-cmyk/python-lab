a = input("Enter the first list of integers: ").split()
a = [int(i) for i in a] 
b= input("Enter the second list of integers : ").split()
b= [int(i) for i in b] 
if len(a)==len(b):
    print("same length")
else:
    print("not same")
if sum(a)==sum(b):
    print("sum is same")
else:
    print("sum is different")
for item in a:
     if item in b:
         print("common value found:",item)
         break
else:
    print("no common values found")
 

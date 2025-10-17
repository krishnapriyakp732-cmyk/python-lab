def read_number():
    num=int(input("Enter a number with at least 4 digits: "))
    while num<1000:
        num=int(input("Please enter a number with at least 4 digits: "))
    return num
def reverse_number(num):
    rev=0
    while num>0:
        rev=rev*10+num%10
        num//=10
    return rev
number=read_number()
reversed_num = reverse_number(number)
print("Original number:", number)
print("Reversed number:", reversed_num)

string = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = len([i for i in string if i in vowels])
print(count)

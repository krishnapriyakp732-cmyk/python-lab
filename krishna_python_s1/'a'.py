names = ['Alice','Amanda','Brian','Aaron','Samantha','Dana']
count = sum(name.lower().count('a')
for name in names
print("Total occurrences of 'a': {count}")

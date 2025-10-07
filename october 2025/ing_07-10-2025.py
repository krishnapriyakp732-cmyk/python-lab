word=input("enter a word:")
if len(word)>=3:
    if word[-3:]=='ing':
        word+='ly'
    else:
        word+='ing'
print(word)

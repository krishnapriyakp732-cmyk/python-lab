text="this is asample line ihis is a text"
words=text.split()
counts={}
for words in words:
    counts[words]=counts.get(words,0)+1
print(counts)    
    

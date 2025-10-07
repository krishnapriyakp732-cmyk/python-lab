words = input("Enter words separated by spaces: ").split()
def longest_word_length(words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest
print("Length of the longest word:", longest_word_length(words))

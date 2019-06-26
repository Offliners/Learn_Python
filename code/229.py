# reverse the words in a sentence

text = "Hello, dear World!"

words = text.split() # split by space
words.reverse()

text = " ".join(words)
print(text) # reversed

# Output:
# World! dear Hello,

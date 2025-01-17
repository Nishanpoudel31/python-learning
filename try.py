#create a program that calculate length and total words in a string using user input.
paragraph = input("enter the paragraph here:")
length = len(paragraph)
words = paragraph.split(' ')
number_of_words = len(words)
print(f"The length of the above given paragraph is : {length}")
print(f"The number of words in given paragraph is : {number_of_words}")
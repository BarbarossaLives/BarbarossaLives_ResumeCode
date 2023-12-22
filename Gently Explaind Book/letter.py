word_without_vowels = ""

# Prompt the user to enter a word
user_word = input("Enter a word.")
user_word = user_word.upper
# user_word = user_word.upper
# and assign it to the user_word variable.


for letter in user_word:
    print(type(letter))
    print(letter)
    if letter== "A" or letter=="E" or letter=="I" or letter =="O" or letter=="U":
        continue
    else:
        print(letter)
        word_without_vowels = word_without_vowels + letter
    

# Print the word assigned to word_without_vowels.
print(word_without_vowels)
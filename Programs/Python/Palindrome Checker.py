word = input('Enter a word:')
print("\n________________________________")
wordBack = word[::-1]
print(wordBack)
if word==wordBack:
    print("\nIt is a palindrome")
else:
    print("\nIt is NOT a palindrome")
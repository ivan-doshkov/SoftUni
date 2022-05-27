words = input().split(" ")
palindrom = input()
list = []

for word in words:
    rev_word = reversed(word)
    rev_word1 = "".join(rev_word)
    if rev_word1 == word:
        list.append(word)
print(list)
pal_count = words.count(palindrom)
print(f"Found palindrome {pal_count} times")


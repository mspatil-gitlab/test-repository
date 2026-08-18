sentence = "apple banana apple orange banana apple"

word_count = {}
# print(sentence.split())

for word in sentence.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count) # Output:  {'apple': 3, 'banana': 2, 'orange': 1}

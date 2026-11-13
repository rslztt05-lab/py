text = "sain baina sain"
count = {}
for w in text.split():
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
print(count)
dun = {"Bat": 85, "Saraa": 92, "Dorj": 70, "Bold": 78}

niit = 0
for ner in dun:
    niit += dun[ner]
print("Dundaj:", niit / len(dun))

b = max(dun, key=dun.get)
print("Hamgiin undur:", b, dun[b])

for ner in dun:
    if ner[0] == "B":
        print(ner)
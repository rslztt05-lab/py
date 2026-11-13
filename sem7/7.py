dun = {"Bat": [80, 90, 85], "Dorj": [70, 75, 80], "Saraa": [95, 90, 92]}
best = ""
max_avg = 0
for ner in dun:
    avg = sum(dun[ner]) / len(dun[ner])
    if avg > max_avg:
        max_avg = avg
        best = ner
print(best, max_avg)
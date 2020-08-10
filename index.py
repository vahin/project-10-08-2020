import csv
from collections import Counter
from numpy import mean, median

with open("weightHeight.csv", newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
weight = []

for i in range(len(fileData)):
    weight.append(float(fileData[i][2]))

mean = mean(weight)
median = median(weight)

modeCounter = {"70-100":0, "100-150":0, "150-180":0}

for i, j in Counter(weight).items():
    if 70 < i < 100:
        modeCounter["70-100"] += 1
    elif 100 < i < 150:
        modeCounter["100-150"] += 1
    elif 150 < i < 180:
        modeCounter["150-180"] += 1
modeRange, modeOcc = 0, 0

for i, j in modeCounter.items():
    if j > modeOcc:
        modeRange, modeOcc = [int(i.split("-")[0]), int(i.split("-")[1])], j

mode = float(modeRange[0] + modeRange[1]) / 2

print("Average weight: {}".format(mean))
print("Meadian of the weights: {}".format(median))
print("Mode of the weights: {}".format(mode))

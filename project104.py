import csv
from collections import Counter

with open("SOCR-HeightWeight.csv") as f:
  frame = csv.reader(f)
  data = list(frame)

data.pop(0)
newData = []

for i in range(0,len(data)):
  data_new = data[i][2]
  newData.append(float(data_new))

a = 0
s = len(newData)
for i in newData:
  a += i

mean = a/s
print('Mean:',mean)

newData = data[2]
newData.sort()# l = [1,2,3,2,4,6,4,8,7,3,4,7,3,3,6]

length = len(newData)

if(length % 2 == 0):
    mid1 = newData[length//2]
    mid2 = newData[(length//2)-1]
    median = (mid1 + mid2)/2
else:
    median = newData[length//2]

print('Median:',median)

data_new = []
for i in newData:
    x = float(i)//1
    data_new.append(x)

datan = Counter(data_new)
temp_dict = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
}

for weight, occurence in datan.items():
    if 75 < weight < 85:
        temp_dict["75-85"] += occurence
    elif 85 < weight < 95:
        temp_dict["85-95"] += occurence
    elif 95 < weight < 105:
        temp_dict["95-105"] += occurence
    elif 105 < weight < 115:
        temp_dict["105-115"] += occurence
    elif 115 < weight < 125:
        temp_dict["115-125"] += occurence
    elif 125 < weight < 135:
        temp_dict["125-135"] += occurence
    elif 135 < weight < 145:
        temp_dict["135-145"] += occurence
    elif 145 < weight < 155:
        temp_dict["145-155"] += occurence
    elif 155 < weight < 165:
        temp_dict["155-165"] += occurence
    else:
        temp_dict["165-175"] += occurence

mode_range, mode_occurence = 0, 0

for range, occurence in temp_dict.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split('-')[0]), int(range.split('-')[1])], occurence
mode = float((mode_range[0]+mode_range[1])/2)
print("Mode:",mode)
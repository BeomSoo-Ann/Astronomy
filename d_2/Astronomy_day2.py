from turtle import color
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import datetime
import sys

file = '/Users/annbeomsu/projects/Astronomy/d_2/VOYAGER1_COHO1HR_MERGED_MAG_PLASMA_2.txt'
full_text = open(file, 'r')

date = []
time = []
distance = []
magnetic = []
proton = []

n = 0

while True:
    line = full_text.readline()

    if not line:
        break
    if '#' in line:
        continue

    n += 1
    columns = line.split()

    if n == 1:
        header = columns
        continue
    if n == 2:
        units = columns
        continue

    if float(columns[3]) <= -1e30 or float(columns[4]) <= -1e30:
        continue

    date.append(columns[0])
    time.append(columns[1])
    distance.append(columns[2])
    magnetic.append(columns[3])
    proton.append(columns[4])

dates = []

for i in range(0, len(date)):
    date1 = date[i].split('-')
    time1 = time[i].split(':')
    sec = time1[2].split('.')

    day = int(date1[0])
    month = int(date1[1])
    year = int(date1[2])

    hour = int(time1[0])
    minute = int(time1[1])
    second = int(sec[0])
    msec = int(sec[1])

    one_day = datetime.datetime(year, month, day, hour, minute, second, msec)
    dates.append(one_day)

distance = np.asarray(distance, dtype=float)
magnetic = np.asarray(magnetic, dtype=float)
proton = np.asarray(proton, dtype=float)

x_data = distance
y_data = proton

plt.figure(figsize=(16, 8))
plt.plot(x_data, y_data)
# dates 사용시
# plt.plot_date(dates, y_data)

plt.title("Distance-Proton", fontsize=15)
plt.xlabel("Distance" + " ("+units[2]+")", fontsize=15)
plt.ylabel("Proton"+" ("+units[4]+")", fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(["Proton"], fontsize=15)

plt.axvline(121.6, color="r")
# plt.axvline(121.7, color="y")
# plt.axvline(121.0, color="gray")
# plt.axvline(x=datetime.datetime(2012, 8, 25), color="gray")

plt.show()

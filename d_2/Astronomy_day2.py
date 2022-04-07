import numpy as np
import matplotlib.pyplot as plt
import datetime
import sys

file = 'C:/Users/BumLahm/Desktop/Programing/Astronomy_2/d_2/VOYAGER1_COHO1HR_MERGED_MAG_PLASMA_2.txt'
full_text = open(file, 'r')

date=[]
time=[]
distance=[]
magnetic=[]
proton=[]

n=0

while True:
    
    line = full_text.readline()
    
    if not line:
        break

    if '#' not in line:
        n+=1
        columns = line.split()

        if (n==1):
            header = columns
            #sys.exit(header)
        elif (n==2):
            units = columns
            #sys.exit(units)
        else:
            if (float(columns[3])>-1e30 and float(columns[4])>-1e30):
                date.append(columns[0])
                time.append(columns[1])
                distance.append(columns[2])    
                magnetic.append(columns[3])
                proton.append(columns[4])

dates=[]
for i in range(0,len(date)):
    date1=date[i]
    time1=time[i]

    day=int(date1[0:2])
    month=int(date1[3:5])
    year=int(date1[6:])

    hour=int(time1[0:2])
    minute=int(time1[3:5])
    second=int(time1[6:8])
    msec=int(time1[9:])

    one_day = datetime.datetime(year,month,day,hour,minute,second,msec)
    dates.append(one_day)

distance=np.asarray(distance, dtype=float)
magnetic=np.asarray(magnetic, dtype=float)
proton=np.asarray(proton, dtype=float)

y_data = distance
x_data = dates
# + " ("+units[2]+")"
plt.figure(figsize=(16,8))
plt.plot_date(x_data,y_data)
plt.title("distance-dates",fontsize= 15)
plt.ylabel("distance"+ " ("+units[2]+")", fontsize= 15)
plt.xlabel("dates"+" ("+"yyyy/mm/dd"+")", fontsize= 15)
plt.xticks(fontsize= 15)
plt.yticks(fontsize= 15)
plt.legend(["dates"],fontsize= 15)
plt.axhline(121.6, color="r")
plt.axhline(121.7, color="y")
plt.axhline(121.0, color="gray")
plt.axvline(x=datetime.datetime(2012, 8, 25), color="gray")
plt.show()

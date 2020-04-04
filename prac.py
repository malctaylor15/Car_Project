import csv
import os
import datetime


os.chdir('Car_project')
path = 'demo.txt'
hnd = open(path, 'w')
writer = csv.writer(hnd)

now = datetime.datetime.now()
stop_time = now + datetime.timedelta(seconds=30)

x = 0
while (x<10e3) and (finish_time < stop_time) :
    writer.writerow([x, x+1])
    x = x+1
    finish_time = datetime.datetime.now()


hnd.close()

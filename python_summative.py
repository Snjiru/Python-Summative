import random
import csv
import datetime


#function for the sensor
def sensors():
    sensor_data = []
    for i in range(0,16):
        x = round(random.random(), 2)
        sensor_data.append(x)
    return sensor_data

#function for randomizing the error
def invalid_data():
    data = []
    for i in range(0,16):

        data.append(round(random.random(),2))
    x = random.randint(0,15)
    data[x] = "err"
    return data

#function for sensor cluster
def sensor_cluster():
    cluster = {}
    for i in range(0,32):
        cluster[i + 1] = sensors()

    y = random.randint(1,2)
    if y == 2:
        n = random.randint(1,32)
        cluster[n] = invalid_data()

        f= open("error.txt","a+")
        f.write("There is an error in cluster %d\r\n" % n)
        f.close()

        #print("There is an error in cluster", n)

    return cluster

#writing into a file
with open ("test.txt",'a') as f:
  f.write(str(sensor_cluster()))
  f.write("\n")
  f.close()




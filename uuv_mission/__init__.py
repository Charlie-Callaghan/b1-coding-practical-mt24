# Module for designing the controller

# import numpy, matplotlib and pandas

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import csv
import csv

# define necessary variables for controller
r = []
h = []
d = []
e = []
u = []
Kp = 0.15
KD = 0.6

# open the mission.csv and append the r, h, and d arrays.
with open('b1-coding-practical-mt24/data/mission.csv', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    
    for row in reader:

        r.append(row[0])
        h.append(row[1])
        d.append(row[2])

# create a loop to calculate error

for i in range(len(d)):
    e.append(float(r[i]) - float(d[i]))

    u.append(Kp*float(e[i]) + KD*(float(e[i]) - float(e[i-1])))


print(u)

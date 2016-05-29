from math import *
import numpy as np
import matplotlib.pyplot as plt


r=1
k,x0,x1=1000,0.3,0.7
previous=[]
current=[]
x=[]
for i in range(201):
    previous.append(e**(-k*(float(i)/200.0-x0)**2)+e**(-k*(float(i)/200.0-x1)**2))
    current.append(e**(-k*(float(i)/200.0-x0)**2)+e**(-k*(float(i)/200.0-x1)**2))
    x.append(float(i)/200.0)
current[-1]=0
previous[-1]=0
current[0]=0
previous[0]=0

figure=[]
figure.append(previous)
figure.append(current)

for i in range(420):
    j=1
    new=[0]
    while j<=199:        
    	new.append(2*(1-r**2)*figure[i+1][j]-figure[i][j]+r**2*(figure[i+1][j+1]+figure[i+1][j-1]))
        j=j+1
    new.append(0)
    figure.append(new)


for i in range(420):
    plt.figure(figsize=(8,6))
    plt.xlabel("position(arbitary units)")
    plt.ylabel("displacement(arbitary units)")
    plt.ylim(-1.2,1.2)
    plt.title("Simulation of wave collision")
    plt.plot(x,figure[i+1],linewidth=2)
    plt.legend()
    plt.show()


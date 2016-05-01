#billiard on triangle

#initial position=(0,1)


import numpy as np
import matplotlib.pyplot as plt

x=[0]
y=[1]
vx,vy=1,0.001
time,i,dt=0,0,0.001
sdt=0.00001


while time<=300:
    X=x[i]+vx*dt
    Y=y[i]+vy*dt
    if Y>0:
        if X>=0:
            if Y<-X*4.0/3.0+4:
                x.append(X)
                y.append(Y)
            else:
                x1=x[i]+vx*sdt
                y1=y[i]+vy*sdt
                if y1<-x1*4.0/3.0+4:
                    x.append(x1)
                    y.append(y1)
                else:
                    char1=-vx*0.28-vy*0.96                
                    char2=-vx*0.96+vy*0.28
                    vx=char1
                    vy=char2                
                    x.append(x[i]+vx*sdt)
                    y.append(y[i]+vy*sdt)
        if X<0:
            if Y<X*4.0/3.0+4:
                x.append(X)
                y.append(Y)
            else:
                x2=x[i]+vx*sdt
                y2=y[i]+vy*sdt
                if y2<x2*4.0/3.0+4:
                    x.append(x2)
                    y.append(y2)
                else:
                    char3=-vx*0.28+vy*0.96
                    char4=vx*0.96+vy*0.28
                    vx=char3
                    vy=char4
                    x.append(x[i]+vx*sdt)
                    y.append(y[i]+vy*sdt)
    if Y<=0:
        x3=x[i]+vx*sdt
        y3=y[i]+vy*sdt
        if y3>0:
            x.append(x3)
            y.append(y3)
        else:   
            vy=-vy
            x.append(x[i]+vx*sdt)
            y.append(y[i]+vy*sdt)
    time=time+dt
    i=i+1

plt.figure(figsize=(15,10))
plt.title("vx0=1,vy0=0.001")
plt.xlabel("x")
plt.ylabel("y")
plt.xticks([-3,-2,-1,0,1,2,3])
plt.yticks([0,1,2,3,4])
plt.xlim(-3,3)
plt.ylim(0,4)
plt.plot([0,3],[4,0],color="red",label="isosceles triangle",linewidth=2)
plt.plot([-3,0],[0,4],color="red",linewidth=2)
plt.plot([-3,3],[0,0],color="red",linewidth=2)
plt.plot(x,y,label="trajectory")
plt.scatter(0,1,color="black",alpha=1,linewidth=4,label="initial")
plt.legend()
plt.show()
        

#billiard on triangle

#initial position=(0,1)

from visual import *

x=[0]
y=[1]
vx,vy=1,-1
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

scene=display(width=1200,height=800)
box(pos=vector(0,-1.55,0),size=(7,0.05,0.1),color=color.red)
arrow(pos=(3.2,-1.7,0),axis=vector(-4.5,6,0),fixedwidth=1,shaftwidth=0.05,color=color.red)
arrow(pos=(-3.2,-1.7,0),axis=vector(4.5,6,0),fixedwidth=1,shaftwidth=0.05,color=color.red)
arrow(pos=(0,-0.5,0),axis=vector(0.3,-0.3,0),fixedwidth=1,shaftwidth=0.1,color=color.blue)
j=0
while 500*j<=i:
    sphere(pos=vector(x[500*j],y[500*j]-1.5,0),radius=0.05,color=color.green)
    j=j+1

from math import *
from visual import *

x=[0]
y=[1]
z=[0]
v=31
vx=31
vy=0
vz=0
dt=0.01

w=200*pi/3

ax=-(0.0039+0.0058/(1+exp((31-35)/5)))*v*31
ay=-9.8
az=-4.1*10**(-4)*31*w
ball=sphere(pos=(-6,1,0), radius=0.1,color=color.red)

i=0
while y[i]>=0:
    x.append(x[i]+vx*dt)
    y.append(y[i]+vy*dt)
    z.append(z[i]+vz*dt)
    vx=vx+ax*dt
    vy=vy+ay*dt
    vz=vz+az*dt
    v=(vx**2+vy**2+vz**2)**0.5
    ax=-(0.0039+0.0058/(1+exp((v-35)/5)))*v*vx
    az=-4.1*10**(-4)*vx*w
    i=i+1

box=box(pos=vector(0,0,0),size=(17,0.01,0.8),color=color.green)


j=0
while j<=i:
    ball=sphere(pos=(x[j]-6,y[j],z[j]), radius=0.1,color=color.red)
    j=j+1
#print x[-1],y[-1],z[-1];13.5037105294 -0.0143 -0.265878000108



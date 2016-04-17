from math import *
from visual import *


initialangle=60
theta=[initialangle]
time=[0]
omega,i,dt=0,0,0.01

scene=display(width=3800,height=3600)
arrow(pos=vector(-5,0,0),axis=vector(0,0,1.7), shaftwidth=0.02,fixedwidth=1, color=color.green)
arrow(pos=vector(-5,0,0),axis=vector(0,2.2,0), shaftwidth=0.02,fixedwidth=1, color=color.green)
arrow(pos=vector(-5,0,0),axis=vector(10,0,0), shaftwidth=0.02,fixedwidth=1, color=color.green)
sphere(pos=(-5,1-cos(initialangle*pi/180),sin(initialangle*pi/180)),radius=0.05, color=color.blue)

while time[i]<=100:
    theta.append(theta[i]+(omega-(4.9*sin((theta[i]+0.5*omega*dt)*pi/180))*dt)*dt)
    omega=omega-(9.8*sin((theta[i]+0.5*omega*dt)*pi/180))*dt        
    i=i+1
    time.append(i*dt)

j=1
while 50*j<=i:
    sphere(pos=(time[50*j]/10-5,1-cos(theta[50*j]*pi/180),sin(theta[50*j]*pi/180)),radius=0.05, color=color.red)
    j=j+1

from math import *

coordinate=(1234,455)
def calculation(angle,T):
    x=0
    y=0
    ax=-4*10**(-5)*700**2*cos(angle)
    ay=-4*10**(-5)*700**2*sin(angle)
    vx=700*cos(angle)
    vy=700*sin(angle)
    v=700
    dt=T
    t=0
    while x<=coordinate[0]:
        x=x+vx*dt
        y=y+vy*dt
        ax=-4*10**(-5)*(1-2.18*10**(-5)*y)**2.5*v*vx
        ay=-4*10**(-5)*(1-2.18*10**(-5)*y)**2.5*v*vy
        vx=vx+ax*dt
        vy=vy-9.8*dt+ay*dt
        v=(vx**2+vy**2)**(0.5)
        t=t+T
    return x,y,t

def correction():
    a=0    
    while abs(calculation(a*pi/180,0.01)[1]-coordinate[1])>=100:
        a=a+1
    return a
def furthercorrection():
    A=correction()-1
    while abs(calculation(A*pi/180,0.0001)[1]-coordinate[1])>=1:
        A=A+0.1
    return A,calculation(A*pi/180,0.0001)

print furthercorrection()

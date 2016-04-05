from math import *
import numpy as np
import matplotlib.pyplot as plt

def calculation(angle):
    x=0
    y=0
    ax=-4*10**(-5)*700**2*cos(angle)
    ay=-4*10**(-5)*700**2*sin(angle)
    vx=700*cos(angle)
    vy=700*sin(angle)
    v=700
    dt=0.001
    while y>=0:
        x=x+vx*dt
        y=y+vy*dt
        ax=-4*10**(-5)*(1-2.18*10**(-5)*y)**2.5*v*vx
        ay=-4*10**(-5)*(1-2.18*10**(-5)*y)**2.5*v*vy
        vx=vx+ax*dt
        vy=vy-9.8*dt+ay*dt
        v=(vx**2+vy**2)**(0.5)
    return x
def Maxangle():
    j=0
    maxdistance=1000
    for k in range(900+1):
        value=calculation(j*pi/180)
        if maxdistance<value:
            maxdistance=value
            point=j
        j=j+0.1
    return point
A=Maxangle()
Angle=A*pi/180
print A
X=[0]
Y=[0]
Vx=[700*cos(Angle)]
Vy=[700*sin(Angle)]
V=[700]
Ax=-4*10**(-5)*700**2*cos(Angle)
Ay=-4*10**(-5)*700**2*sin(Angle)
dt=0.001
i=0
while Y[i]>=0:
    X.append(X[i]+Vx[i]*dt)
    Y.append(Y[i]+Vy[i]*dt)
    Ax=-4*10**(-5)*(1-2.18*10**(-5)*Y[i])**2.5*V[i]*Vx[i]
    Ay=-4*10**(-5)*(1-2.18*10**(-5)*Y[i])**2.5*V[i]*Vy[i]
    Vx.append(Vx[i]+Ax*dt)
    Vy.append(Vy[i]-9.8*dt+Ay*dt)
    V.append((Vx[i+1]**2+Vy[i+1]**2)**(0.5))
    T=(i+1)*dt
    i=i+1
print X[i],Y[i],T

plt.figure(figsize=(14,9))
plt.ylim(0,8000) 
plt.xlim(0,30000) 
plt.xticks([0,5000, 10000, 15000, 20000,25000,30000],[r'$0$', r'$5$', r'$10$', r'$15$', r'$20$',r'$25$',r'$30$'])
plt.yticks([0,2000, 4000, 6000, 8000],[r'$0$', r'$2$', r'$4$', r'$6$', r'$8$'])
plt.xlabel("X(km)")
plt.ylabel("Y(km)") 
plt.title("Cannon shell trajectory with density correction") 
plt.plot(X, Y, color="red",  linewidth=1.5, linestyle="-", label="x")
plt.legend(loc='upper left', frameon=False)
plt.show()

    



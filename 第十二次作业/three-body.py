from math import *
import numpy as np
import matplotlib.pyplot as plt



mevms=3*10**(-6)
mjvms=1*9.5*10**(-4)


x_earth=[1]
y_earth=[0]
vx_earth=0
vy_earth=2*pi

x_jupiter=[5.2]
y_jupiter=[0]
vx_jupiter=0
vy_jupiter=2.7553590302269777

x_sun=[0]
y_sun=[0]
vx_sun=0
vy_sun=-mevms*2*pi-mjvms*2.7553590302269777

dt=0.0001
i,time=0,0
while time<=30:
    r1=((x_earth[i]-x_sun[i])**2+(y_earth[i]-y_sun[i])**2)**0.5
    r2=((x_jupiter[i]-x_sun[i])**2+(y_jupiter[i]-y_sun[i])**2)**0.5
    r_ej=((x_earth[i]-x_jupiter[i])**2+(y_earth[i]-y_jupiter[i])**2)**0.5
    
    vx_earth=vx_earth-4*(pi**2)*(x_earth[i]-x_sun[i])*dt/r1**3-4*(pi**2)*mjvms*(x_earth[i]-x_jupiter[i])*dt/r_ej**3
    vy_earth=vy_earth-4*(pi**2)*(y_earth[i]-y_sun[i])*dt/r1**3-4*(pi**2)*mjvms*(y_earth[i]-y_jupiter[i])*dt/r_ej**3
    x_earth.append(x_earth[i]+vx_earth*dt)
    y_earth.append(y_earth[i]+vy_earth*dt)
    
    
    vx_jupiter=vx_jupiter-4*(pi**2)*(x_jupiter[i]-x_sun[i])*dt/r2**3+4*(pi**2)*mevms*(x_earth[i]-x_jupiter[i])*dt/r_ej**3
    vy_jupiter=vy_jupiter-4*(pi**2)*(y_jupiter[i]-y_sun[i])*dt/r2**3+4*(pi**2)*mevms*(y_earth[i]-y_jupiter[i])*dt/r_ej**3
    x_jupiter.append(x_jupiter[i]+vx_jupiter*dt)
    y_jupiter.append(y_jupiter[i]+vy_jupiter*dt)

    vx_sun=vx_sun+dt*4*pi**2*mevms*(x_earth[i]-x_sun[i])/r1**3+dt*4*pi**2*mjvms*(x_jupiter[i]-x_sun[i])/r2**3
    vy_sun=vy_sun+dt*4*pi**2*mevms*(y_earth[i]-y_sun[i])/r1**3+dt*4*pi**2*mjvms*(y_jupiter[i]-y_sun[i])/r2**3
    x_sun.append(x_sun[i]+vx_sun*dt)
    y_sun.append(y_sun[i]+vy_sun*dt)
    
    i=i+1
    time=time+dt
    

c=(6*10**24*(x_earth[0]**2+y_earth[0]**2)**0.5+1.9*10**27*(x_jupiter[0]**2+y_jupiter[0]**2)**0.5)/(6*10**24+1.9*10**27+2*10**30)
plt.figure(figsize=(12,12), dpi=80) 
plt.xlim(-6,6)
plt.ylim(-6,6)
plt.xlabel("x(AU)")
plt.ylabel("y(AU)")
plt.title("Simulation of three-body")
plt.plot(x_earth,y_earth,label="Earth",color="blue")
plt.plot(x_jupiter,y_jupiter,label="Jupiter",color="brown")
plt.plot(x_sun,y_sun,label="Sun",color="red")
plt.scatter(c,0,label="center of mass",color="green")
plt.legend()
plt.show()

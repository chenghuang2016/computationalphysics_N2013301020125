from math import *
import numpy as np
import matplotlib.pyplot as plt


theta=[0.2]
omega=[0]
time=[0]
dt,i,n=0.01,0,0


while time[i]<=7000:    
    omega.append(omega[i]+(-sin(theta[i])-0.5*omega[i]+1.2*sin(time[i]*2/3))*dt)
    char=theta[i]+omega[i+1]*dt
    if theta[i]+omega[i+1]*dt<-pi:        
        theta.append(char+2*pi)
    elif theta[i]+omega[i+1]*dt>pi:
        theta.append(char-2*pi)
    else:
        theta.append(char)
    time.append(time[i]+dt)    
    i=i+1

plt.figure(figsize=(14,9))
plt.title("$\omega$ versus $\Theta$,FD=1.2,$\Theta$(0)=0.2,$\omega$(0)=0")
plt.xlim(-4,4)
plt.ylim(-3,1)
plt.xlabel("$\Theta$(radians)")
plt.ylabel("$\omega$(radians/s)")
while 3*n*pi<=time[-1]:
     plt.scatter(theta[int(3*n*pi/dt)],omega[int(3*n*pi/dt)],linewidth=0.01)
     n=n+1
plt.show()

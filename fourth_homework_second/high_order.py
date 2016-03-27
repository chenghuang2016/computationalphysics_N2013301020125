 #import
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

 #set array and initial value
v=[]
x=[]
t=[]
v.append(0)
x.append(2)
t.append(0)
total_time=20
dt=0.0001
N=total_time/dt

 #calculation
for i in range(int(N)):
    v.append(v[i]-9*x[i]*dt-9/2*v[i]*dt**2+27/2*x[i]*dt**3)
    x.append(x[i]+v[i]*dt-9/2*x[i]*dt**2-3/2*v[i]*dt**3)
    t.append(dt*(i+1))

 #print value
for j in range(int(N)+1):
    print t[j],v[j],x[j]

 #plot figure
plt.figure(figsize=(14,9))
 #set ticks
plt.xticks([0,np.pi*2/3, np.pi*4/3, np.pi*2, np.pi*8/3,np.pi*10/3,np.pi*4,np.pi*14/3,np.pi*16/3,np.pi*6,np.pi*20/3],
       [r'$0$', r'$2\pi/3$', r'$4\pi/3$', r'$2\pi$', r'$8\pi/3$',r'$10\pi/3$',r'$4\pi$',r'$14\pi/3$',r'$16\pi/3$',r'$6\pi$',r'$20\pi/3$',])
 #3D effect
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
 #plot v and x
plt.plot(t, v, color="blue", linewidth=1.5, linestyle="-", label="v")
plt.plot(t, x, color="red",  linewidth=1.5, linestyle="-", label="x")
plt.legend(loc='upper left', frameon=False)
 #plot auxiliary line
plt.plot([0,20],[6,6], color ='black', linewidth=1, linestyle="--")
plt.plot([0,20],[0,0], color ='black', linewidth=1, linestyle="--")
plt.plot([0,20],[-6,-6], color ='black', linewidth=1, linestyle="--")
plt.plot([np.pi*2/3,np.pi*2/3],[-8,6], color ='black', linewidth=1, linestyle="--")
plt.plot([np.pi*4/3,np.pi*4/3],[-8,6], color ='black', linewidth=1, linestyle="--")
plt.plot([np.pi*2,np.pi*2],[-8,6], color ='black', linewidth=1, linestyle="--")
plt.plot([np.pi*8/3,np.pi*8/3],[-8,6], color ='black', linewidth=1, linestyle="--")
 #show
plt.show()


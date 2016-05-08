from math import *
import numpy as np
import matplotlib.pyplot as plt
rate=[]
eccentricities=[]
e=0.2
de=0.01

dt=0.0001

alpha=0.01
while e<1:
    x=[0.30966*(1+e)/(1-e)] 
    y=[0]
    vx=0   
    vy=2*pi*(1-e)/(0.30966*(1+e))**0.5
    time,i,j=0,0,1
    while time<=3:
        radius=(x[i]**2+y[i]**2)**0.5
        vx=vx-(1+alpha/radius**2)*4*(pi**2)*x[i]*dt/radius**3
        vy=vy-(1+alpha/radius**2)*4*(pi**2)*y[i]*dt/radius**3
        x.append(x[i]+vx*dt)
        y.append(y[i]+vy*dt)
        time=time+dt
        i=i+1

    plt.figure(figsize=(10,10), dpi=80)
    plt.xlim(-0.6,6)
    plt.ylim(-1,4)
    plt.xlabel("x(AU)")
    plt.ylabel("y(AU)")
    plt.title("Simulation of the precession,e="+str(e))
    plt.plot(x,y,label="trajectory")
    plt.plot([0,x[0]],[0,y[0]])
    x1=[]
    y1=[]
    theta=[]
    time1=[]
    while j<=i-1:
        if (x[j]**2+y[j]**2)**0.5-(x[j-1]**2+y[j-1]**2)**0.5>0 and (x[j]**2+y[j]**2)**0.5-(x[j+1]**2+y[j+1]**2)**0.5>0:
            x1.append(x[j])
            y1.append(y[j])
            time1.append(dt*j)
            if x[j]>=0 and y[j]/x[j]>=0:
                theta.append(atan(y[j]/x[j])*180/pi)
            elif x[j]<0 and y[j]/x[j]<0:
                theta.append(atan(y[j]/x[j])*180/pi+180)
            elif x[j]<0 and y[j]/x[j]>=0:
                theta.append(atan(y[j]/x[j])*180/pi+180)
            elif x[j]>=0 and y[j]/x[j]<0:
                theta.append(atan(y[j]/x[j])*180/pi+360)
            plt.plot([0,x[j]],[0,y[j]])
        j=j+1

#print time1,theta


    
    def degree():
        total_theta,total_time1=0,0
        total_theta_square,total_time1_square,total_theta_time1_square=0,0,0
        for k in range(5):
            total_theta=total_theta+theta[k]
            average_theta=float(total_theta)/float(5)
            total_time1=total_time1+time1[k]
            average_time1=float(total_time1)/float(5)
            total_theta_square=total_theta_square+theta[k]**2
            average_theta_square=float(total_theta_square)/float(5)
            total_time1_square=total_time1_square+time1[k]**2
            average_time1_square=float(total_time1_square)/float(5)
            total_theta_time1_square=total_theta_time1_square+theta[k]*time1[k]
            average_theta_time1_square=float(total_theta_time1_square)/float(5)
        a_degree=float((average_theta_time1_square-average_theta*average_time1))/float((average_time1_square-average_time1**2))
        b_degree=float((average_time1_square*average_theta-average_time1*average_theta_time1_square))/float((average_time1_square-average_time1**2))
        x_degree=np.linspace(0, 3, 256,endpoint=True)
        y_degree=a_degree*x_degree+b_degree
        plt.figure(figsize=(10,10), dpi=80)
        plt.xlabel("time(yr)")
        plt.ylabel("$\Theta$(degrees)")
        plt.title("Orbit orientation versus time,e="+str(e))
        plt.xlim(0,3)
        plt.ylim(0,360)
        plt.scatter(time1,theta,label="numerical result")
        plt.plot(x_degree,y_degree,label="least-squares fit")
        plt.show()
        rate.append(a_degree)
    degree()
    print e
    
    eccentricities.append(e)
    e=e+de
    if e>0.9:
        break

plt.figure(figsize=(12,9), dpi=80)
plt.xlabel("eccentricity")
plt.ylabel("d$\Theta$/dt(degrees/yr)")
plt.title("Simulation of the precession")
plt.plot(eccentricities,rate)
plt.show()
    


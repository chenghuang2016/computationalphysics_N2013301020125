from math import *
from visual import *


def magnet(x0,y0,z0):
    theta=0
    dtheta=0.1
    B_x,B_y,B_z=0,0,0
    while theta<=2*pi:
        x=(sin(40*theta)+3)*cos(theta)
	y=(sin(40*theta)+3)*sin(theta)
	z=cos(40*theta)

	dx=-((40*cos(40*theta))*sin(theta))*dtheta
	dy=((40*cos(40*theta))*cos(theta))*dtheta
	dz=-(40*sin(40*theta))*dtheta

	r_cube=((x0-x)**2+(y0-y)**2+(z0-z)**2)**0.5

	B_x=B_x+((z0-z)*dy-(y0-y)*dz)/r_cube
	B_y=B_y+(-(z0-z)*dx+(x0-x)*dz)/r_cube
	B_z=B_z+((y0-y)*dx-(x0-x)*dy)/r_cube
        theta=theta+dtheta
    return B_x,B_y,B_z

       
x_pos=[]
y_pos=[]
z_pos=[]
k=0
r=5
while k<=3: 
    dalta=0 
    while dalta<=2*pi:
    	x_pos.append(r*cos(dalta))
    	y_pos.append(r*sin(dalta))
    	z_pos.append(k)
    	dalta=dalta+0.1
    k=k+1


B_X=[]
B_Y=[]
B_Z=[]
num=0
while num<=len(x_pos)-1:
    B_X.append(magnet(x_pos[num],y_pos[num],z_pos[num])[0])
    B_Y.append(magnet(x_pos[num],y_pos[num],z_pos[num])[1])
    B_Z.append(magnet(x_pos[num],y_pos[num],z_pos[num])[2])
    num=num+1

theta1=0
x1=[]
y1=[]
z1=[]
while theta1<2*pi:
    x1.append((sin(40*theta1)+3)*cos(theta1))
    y1.append((sin(40*theta1)+3)*sin(theta1))
    z1.append(cos(40*theta1))
    theta1=theta1+0.005

scene=display(width=800,height=800)
c=curve(radius=0.05)
c.x=x1
c.y=y1
c.z=z1
arrow(pos=(0,0,0),axis=vector(8,0,0),fixedwidth=1,shaftwidth=0.05,color=color.green)
arrow(pos=(0,0,0),axis=vector(0,8,0),fixedwidth=1,shaftwidth=0.05,color=color.green)
arrow(pos=(0,0,0),axis=vector(0,0,4),fixedwidth=1,shaftwidth=0.05,color=color.green)
i=0
while 4*i<=len(z_pos):
    arrow(pos=(x_pos[4*i],y_pos[4*i],z_pos[4*i]),axis=vector(B_X[4*i]/20,B_Y[4*i]/20,B_Z[4*i]/20),fixedwidth=1,shaftwidth=0.05,color=color.red)
    i=i+1

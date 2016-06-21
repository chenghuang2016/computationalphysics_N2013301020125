from math import *
from pylab import *
import random

r=1.5*10**(-15)
R=0.53*10**(-10)
'''    
1,35000
'''

hbar=1.05457*10**(-34)
Mp=1.67262*10**(-27)
Me=9.10938*10**(-31)
m=Mp*Me/(Me+Mp)
a=hbar**2/(2*m)
dx=dy=dy=3500*r

e=1.6*10**(-19)
epsilon=8.85419*10**(-12)
b=-e**2/(4*pi*epsilon)

Psi=1/((2*R)**1.5)

psi=[]
for l in range(21):
    psi.append([])
    for m in range(21):
        psi[l].append([])
	for n in range(21):
	    psi[l][m].append(Psi)

def energy():
    for i in range(20-1):
	for j in range(20-1):
	    for k in range(20-1):
		E=-a*psi[i+1][j+1][k+1]*((psi[i+2][j+1][k+1]+psi[i][j+1][k+1]-2*psi[i+1][j+1][k+1])/dx**2)
		E=E-a*psi[i+1][j+1][k+1]*((psi[i+1][j+2][k+1]+psi[i+1][j][k+1]-2*psi[i+1][j+1][k+1])/dx**2)
		E=E-a*psi[i+1][j+1][k+1]*((psi[i+1][j+1][k+2]+psi[i+1][j+1][k]-2*psi[i+1][j+1][k+1])/dx**2)
		E=E+((psi[i+1][j+1][k+1])**2)*b/(r*(((3500*(i+1-10))**2+(3500*(j+1-10))**2+(3500*(k+1-10))**2)**0.5)+r)
    E=E*(dx**3)
    return(E)

def normalization():
    normal=0
    for i in range(21):
	for j in range(21):
	    for k in range(21):
		normal=normal+(psi[i][j][k])**2
    normal=1/(normal*(dx**3))
    return(normal)

iterations=600000    
for n in range(iterations):
    Energy=energy()
    u=random.randint(0,20)
    v=random.randint(0,20)
    w=random.randint(0,20)
    dpsi=(random.uniform(-1,1))*Psi
    psi[u][v][w]=psi[u][v][w]+dpsi
    char1=normalization() 
    char=energy()*char1
    if char<Energy:   
        for i in range(21):
            for j in range(21):
	        for k in range(21):
                    psi[i][j][k]=psi[i][j][k]*(char1**0.5)

    else:
	psi[u][v][w]=psi[u][v][w]-dpsi
print iterations,Energy/(1.60217*10**(-19))
#fout=open('/home/jack/comeout.txt','w')
#fout.write(str(psi))


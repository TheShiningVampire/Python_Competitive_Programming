import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib as mpl

#SCF Method
#Constants
q = 1.6e-19
hbar = 1.055e-34
I0 = (q**2)/hbar
#print(hbar)

#input parameters
mu = 0
eps = 0.2 #in eV
kT = 0.025 #k_b*T in eV
g1 = 0.005
g2 = 0.0005 #in eV
g = g1 + g2
Vg = 0 #gate voltage is taken to be 0
Vd = 0  #drain voltage, initially 0UL = 0 #-(q*Vd)/2
U0 = 0.25 #single electron charging energy in eV
gate_c = 1 #Cg/Ce
drain_c = 0.5 #Cd/Ce
alpha = 0.1

NE=401
E = np.linspace(-18*g,18*g,NE)#Let E be the spreading density= 97 %
dE = E[2]-E[1]
D =(g/(2*math.pi))/(((E)**2)+((g/2)**2)) #Lorentzian Density of states, D(E'-U)
#E' = E+U+eps+UL => F1(E')= F1(E+U+eps+UL), similarly F2
D = D/(dE*sum(D))#Normalizing to one

maxD = np.amax(D)

#print(D[2])

#input values to be considered
IV_char = 401
Vd = -.65
N = np.zeros(IV_char)
I = np.zeros(IV_char)

for i in range(IV_char):
    mu1 = mu
    mu2 = mu1 - Vd
    UL=-(gate_c*Vg)-(drain_c*Vd)
    #print(UL[199])

    #Let U be the Self Cosistent Field
    U = 0
    dU = 1 #initializing the initial difference between calc. vs SCF

    while dU > 1e-6:
        F1 = 1/(1+np.exp((E+U+eps+UL - mu1)/kT))
        F2 = 1/(1+np.exp((E+U+eps+UL - mu2)/kT))
        N[i] = dE*sum(np.multiply(D, (g1*F1+g2*F2)/(g)))
        U_new = np.multiply(U0, N[i])
        dU = abs(U_new - U)
        U = U + alpha*(U_new - U)

print(N[1])

x1=np.linspace(0,1.5,401)
x2=np.linspace(1.5,3,401)
x3=np.linspace(3,4.5,401)

Mu1 = np.zeros(401)
U1 = np.zeros(401)
Mu2 = np.zeros(401)
nocharging = np.zeros(401)
j=0


while j<401:
    Mu1[j] = mu1
    U1[j] = U+eps+UL
    Mu2[j] = mu2
    nocharging[j] = eps-Vd/2 
    j=j+1

mpl.rcParams['lines.linewidth'] = 2.5
mpl.rcParams['lines.linestyle'] = '-'
plt.plot(x1,Mu1)
plt.plot(x2,U1)
plt.plot(x3,Mu2)
plt.plot(((D*1.5)/maxD)+1.5,E+U1)
mpl.rcParams['lines.linewidth'] = 2.5
mpl.rcParams['lines.linestyle'] = '--'
plt.plot(x2 , nocharging, label= 'No charging effects')  #considering no charging
plt.xticks([0.75, 2.25, 3.75], ['Source', 'Channel', 'Drain'])
plt.grid(linestyle='-', linewidth=0.5)
plt.show()
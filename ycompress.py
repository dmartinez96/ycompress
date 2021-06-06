# Import Libraries
import numpy as np

# Izzyjet
eta_n = 0.9
gamma_n = 1.36
R = 287.05
Q_R = 45000
cp = R*((gamma_n) / (gamma_n - 1))

Ta = 288.2
gamma_d = 0.97
M = 0
T02 = Ta*(1 + ((gamma_d - 1) / 2)*M^2)
T03 = 1500
f = ((T03/T02) - 1) / ((Q_R/cp * T02) - (T03/T02))
print(f)
ue = np.sqrt(2*eta_n*(gamma_n / (gamma_n -1))*R*T06*(1 - (pa/p06)^((gamma_n - 1)/gamma_n)))
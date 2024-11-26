import scipy.integrate as spi
import numpy as np
import pylab as plt

b = 1
gamma = 1/5
TS = 1
ND = 200
S0 = 0.99
I0 = 0.01
pb = 0.4


def diff_eqs(INP, t):
	Y = np.zeros((3))
	V = INP
	if t < Tau:
		Ps = t/(2*Tau)
	else:
		Ps = 1/2
	beta = b*(1-pb)
	Y[0] = - beta * (1-V[1]-V[2]-Ps) * V[1]
	Y[1] = beta * (1-V[1]-V[2]-Ps) * V[1] - gamma * V[1]
	Y[2] = gamma * V[1]
	return Y


INPUT = (S0, I0, 0.0)
Tau_list = [0, 20, 30, 50, 100, 500]
R_list = []
for Tau in Tau_list:
    t_start = 0.0
    t_end = ND
    t_inc = TS
    t_range = np.arange(t_start, t_end+t_inc, t_inc)
    RES = spi.odeint(diff_eqs, INPUT, t_range)
    R_list.append([RES[:, 2], Tau])

t_list = np.linspace(0, 200, num=200)
Ps_list = [[], [], [], [], [], []]
for Tau in Tau_list:
    for t in t_list:
        if t < Tau:
            Ps_list[Tau_list.index(Tau)].append(t/(2*Tau))
        else:
            Ps_list[Tau_list.index(Tau)].append(1/2)

plt.figure(figsize=(20, 6), dpi=100)
plt.suptitle(
	'Dynamics of the recovered (R) when the density of prevention Ps increases in the SIR model')

plt.subplot(121)
for i in range(6):
    plt.plot(t_list, Ps_list[i], label='Tau={}'.format(Tau_list[i]))
plt.xlabel('Time(day)')
plt.ylabel('density of Prevention (Ps)')
plt.legend(loc=0)
plt.grid(color='navy', linestyle='--', linewidth=0.5)

plt.subplot(122)
for i in R_list:
    plt.plot(i[0], lw=2, label='Tau={}'.format(i[1]))
plt.legend(loc=0)
plt.xlabel('Time(day)')
plt.ylabel('density of Recovereds (R∞)')
plt.grid(color='navy', linestyle='--', linewidth=0.5)

plt.savefig('SIR-MFT (delay)')

import scipy.integrate as spi
import numpy as np
import pylab as plt

b = 1
gamma = 1/5
TS = 0.1
ND = 70
S0 = 0.99
I0 = 0.01


def diff_eqs(INP, t):
	Y = np.zeros((3))
	V = INP
	Y[0] = - beta * V[0] * V[1]
	Y[1] = beta * V[0] * V[1] - gamma * V[1]
	Y[2] = gamma * V[1]
	return Y


pbdata = np.array([0, 0.2, 0.4, 0.6, 0.8])
psdata = np.linspace(0, 1, num=60)
rdata = [[], [], [], [], []]
for pb in pbdata:
    for ps in psdata:
        INPUT = (S0-ps, I0, 0.0)
        beta = b*(1-pb)
        t_start = 0.0
        t_end = ND
        t_inc = TS
        t_range = np.arange(t_start, t_end+t_inc, t_inc)
        rdata[list(pbdata).index(pb)].append(
            spi.odeint(diff_eqs, INPUT, t_range)[:, 2][-1])

plt.figure(dpi=250, figsize=(12, 10))
plt.title('Global interaction against the density of Prevention')
plt.plot(psdata, rdata[0], lw=2, label='Pb=0.0')
plt.plot(psdata, rdata[1], lw=2, label='Pb=0.2')
plt.plot(psdata, rdata[2], lw=2, label='Pb=0.4')
plt.plot(psdata, rdata[3], lw=2, label='Pb=0.6')
plt.plot(psdata, rdata[4], lw=2, label='Pb=0.8')
plt.legend(loc=0)
plt.xlabel('density of Prevention (Ps)')
plt.ylabel('density of Recovereds (R∞)')
plt.grid(color='navy', linestyle='--', linewidth=0.5)
plt.savefig('R(inf)-Ps Global')
plt.show()

psdata = np.array([0, 0.2, 0.4, 0.6, 0.8])
pbdata = np.linspace(0, 1, num=60)
rdata = [[], [], [], [], []]
for ps in psdata:
    for pb in pbdata:
        INPUT = (S0-ps, I0, 0.0)
        beta = b*(1-pb)
        t_start = 0.0
        t_end = ND
        t_inc = TS
        t_range = np.arange(t_start, t_end+t_inc, t_inc)
        rdata[list(psdata).index(ps)].append(
            spi.odeint(diff_eqs, INPUT, t_range)[:, 2][-1])

plt.figure(dpi=250, figsize=(12, 10))
plt.title('Global interaction against the density of Quarantine')
plt.plot(pbdata, rdata[0], lw=2, label='Ps=0.0')
plt.plot(pbdata, rdata[1], lw=2, label='Ps=0.2')
plt.plot(pbdata, rdata[2], lw=2, label='Ps=0.4')
plt.plot(pbdata, rdata[3], lw=2, label='Ps=0.6')
plt.plot(pbdata, rdata[4], lw=2, label='Ps=0.8')
plt.legend(loc=0)
plt.xlabel('density of Quarantine (Pb)')
plt.ylabel('density of Recovereds (R∞)')
plt.grid(color='navy', linestyle='--', linewidth=0.5)
plt.savefig('R(inf)-Pb Global')
plt.show()

pbdata = np.linspace(0, 1, num=100)
psdata = np.linspace(0, 1, num=100)
rdata = np.zeros((100, 100))
m = 0
for pb in pbdata:
    n = 0
    for ps in psdata:
        INPUT = (S0-ps, I0, 0.0)
        beta = b*(1-pb)
        t_start = 0.0
        t_end = ND
        t_inc = TS
        t_range = np.arange(t_start, t_end+t_inc, t_inc)
        rdata[m][n] = (spi.odeint(diff_eqs, INPUT, t_range)[:, 2][-1])
        n += 1
    m += 1

plt.figure(dpi=250,figsize=(12,10))
c=plt.pcolormesh(psdata, pbdata, rdata, cmap="plasma")
plt.colorbar(c)
plt.title('density of Quarantine - density of Prevention (Global)')
plt.xlabel('density of Prevention (Ps)')
plt.ylabel('density of Quarantine (Pb)')
plt.savefig('Ps-Pb')
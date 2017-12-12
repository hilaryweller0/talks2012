from pylab import *

a=6e6
u0=20.
yc=a
w=0.5*a
g=10.
beta=2e-11
h0=3000.

y = linspace(0.,2*a, 101)
yhat = (y - yc)/w

u = where(abs(yhat) < 1, u0*(1 - 3*yhat**2 + 3*yhat**4 - yhat**6), 0.0)

h = where(yhat < -1, h0, \
          where(yhat < 1, \
                h0 - w*beta*u0/g*(\
                  yc*(16/35.+ yhat - yhat**3 + 3/5.*yhat**5 -1/7.*yhat**7)\
     + w*(-1/8. + 0.5*yhat**2 - 0.75*yhat**4 + 0.5*yhat**6 -1/8.*yhat**8)),\
                h0 - 32./35.*w*beta*u0*yc/g))

clf()
ion()
ax1 = subplot(111)
plot(u,1e-3*y,'r', label='u')
legend(loc=1)
xlabel('u (m/s)')
ylabel('y (km)')
ax2 = twiny()
plot(h,1e-3*y, label='h')
xlabel('h (m)')
legend(loc=9)

savefig('jetProfile.pdf')


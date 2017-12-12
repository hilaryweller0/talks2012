from pylab import *

a=6e6
u0=80.
yc=a
w=0.25*a
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

vort0 = 6*u0/w;
vort = where(abs(yhat) < 1, vort0*yhat*(1 - 2*yhat**2 + yhat**4), 0.0)

clf()
ion()
plot(u/u0,1e-3*y,'r', label=r'$u/u_0$')
plot(h/h0,1e-3*y,'b', label=r'$h/h_0$')
plot(vort/1e-4, 1e-3*y, 'k', label=r'$\xi\times 10^4 s^{-1}$')
legend(loc=2)
ylabel('y (km)')

savefig('thinJetProfile.pdf')


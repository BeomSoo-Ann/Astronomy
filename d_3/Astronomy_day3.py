import numpy as np
import pandas as pd
from astropy.timeseries import LombScargle
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

lin = pd.read_csv('LINEAR_11375941.csv')

#NEOWISE_DATA
n1 = pd.read_csv('neowise_yso5.csv')
nq1 = n1[n1['qual_frame'] > 0]
mjd1 = nq1.mjd
mag1 = nq1.w2mpro
emag1 = nq1.w2sigmpro

fig, ax = plt.subplots()
ax.errorbar(mjd1, mag1, emag1, fmt='.')
ax.invert_yaxis()
ax.set_ylabel('magnitude', size=12)
ax.set_xlabel('mjd', size=12)
plt.show()

#periodogram_analysis
fig0, ax0 = plt.subplots(figsize=(10,4))
ax0.errorbar(lin.t, lin.mag, lin.magerr, fmt='.k', ecolor='gray', capsize=0)
ax0.invert_yaxis()
ax0.set_ylabel('magnitude')
ax0.set_xlabel('mjd')
ax0.set_title('Lightcurve : Linear object 11375941')
plt.show()

lsav = LombScargle(lin.t, lin.mag, lin.magerr) #class LombScargle

#claculate frequency and power in given frequency
frequency, power = lsav.autopower(nyquist_factor=500, minimum_frequency=0.2)

period_days = 1. / frequency
period_hours = period_days * 24

best_period = period_days[power==max(power)][0] #best period as frequency with maximum power
phase = (lin.t / best_period) % 1 # time = period * (x + phase)
                                  # --> time/period = x + phase (0<phase<1)
                                  # --> (time/period) % 1 = phase
print("Best period: {0:.2f} days/ power : {1:.3f}".format(best_period, np.max(power)))

fig, ax = plt.subplots(1, 2, figsize=(8, 3))
ax[0].plot(period_days, power, '-k')
ax[0].set(xlim=(0, 2.5), xlabel='Period (days)', ylabel='Lomb-Scargle Power', title='Lomb-Scargle Periodogrma')

ax[1].errorbar(phase, lin.mag, lin.magerr, fmt='.k', ecolor='gray', capsize=0)
ax[1].set(xlabel='phase', ylabel='magnitude', title='Phased Data')
ax[1].invert_yaxis()
ax[1].text(0.02, 0.03, "Period = {0:.2f} days ({0:.2f} hours)".format(best_period, best_period*24), transform=ax[1].transAxes)
ax[1].set_xlim(0, 1)
#left=Periodogram itself
plt.show()

#NEOWISE
lsav = LombScargle(mjd1, mag1, emag1)

max_period = 10000
min_period = 200
frequency, power = lsav.autopower(minimum_frequency=1/max_period, maximum_frequency=1/min_period)

period_days = 1. / frequency
period_hours = period_days * 24

best_frequency = frequency[power==max(power)][0]
best_period = period_days[power==max(power)][0]
phase = (mjd1 / best_period) % 1 

print("Best period: {0:.2f} days/ power : {1:.3f}".format(best_period, np.max(power)))

fig, ax = plt.subplots(1, 2, figsize=(8, 3))
ax[0].plot(period_days, power, '-k')
ax[0].set(xlabel='Period (days)', ylabel='Lomb-Scargle Power', title='Lomb-Scargle Periodogrma')
ax[0].set_xscale('log')

ax[1].errorbar(phase, mag1, emag1, fmt='.k', ecolor='gray', capsize=0)
ax[1].set(xlabel='phase', ylabel='magnitude', title='Phased Data')
ax[1].invert_yaxis()
ax[1].text(0.02, 0.03, "Period = {0:.2f} days ({1:.2f} hours)".format(best_period, best_period*24), transform=ax[1].transAxes)
ax[1].set_xlim(0, 1)
plt.show()

fig3, ax3 = plt.subplots()
smjd = np.linspace(min(mjd1), max(mjd1), 1000)
flux_jmod = lsav.model(smjd, best_frequency)
ax3.errorbar(mjd1, mag1, emag1, fmt='k.', label='data')
ax3.plot(smjd, flux_jmod, 'r-', label='model')
ax3.invert_yaxis()
ax3.set_ylabel('mag')
ax3.set_xlabel('mjd')
ax3.legend()

plt.show()
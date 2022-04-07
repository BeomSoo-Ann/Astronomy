import astropy.io.fits as fits
import matplotlib.pyplot as plt
import numpy as np
import astropy.io.ascii as ascii

fits_data= fits.open("spec-2241-54169-0592.fits")
fits_data1= fits.open("frame-r-005115-5-0153.fits")
file= "SDSS_galaxies_add10.txt"

image= fits_data1[0].data
header= fits_data1[0].header

image= np.array(image)

max_value= np.percentile(image, 99.8)
min_value= np.percentile(image, 20)

plt.figure(figsize=(14,10))
plt.imshow(image, cmap='gray', vmax= max_value, vmin= min_value, origin='lower')
plt.show()


spectrum= fits_data[1].data

flux= []
loglam= []

for i in range(len(spectrum)):
    flux.append(spectrum[i][0])
    loglam.append(spectrum[i][1])

flux= np.array(flux)
lam= 10**np.array(loglam)

real_line= 6585.268
test_line= 6705.3


plt.figure(figsize=(14,10))
plt.plot(lam,flux)
plt.title("[Spectrum lines of NGC4921]")
plt.xlabel('Wavelength (Angstroms)')
plt.ylabel('Flux (10^-7 erg/s/cm^2/Ang)')
plt.vlines(real_line, 0, 200, colors='red')
plt.vlines(test_line, 0, 200, colors='green')
plt.show()

#redshift value
z_value= test_line/real_line-1
print('z= ', z_value)
#recession velocity
velocity= z_value*300000
print('recession velocity= ', velocity, '[km/s]')

#hubble diagram
full_text= ascii.read(file, 'r')
#print(full_text)

data= dict(full_text)

distance= data['Distance (MPc)']
velocity= data['Velocity (km/s)']

eq= np.polyfit(distance, velocity, 1)
fx= np.poly1d(eq)

hubble_const= eq[0]
print("Hubble constant: ", hubble_const, "km/s/Mpc")
Age= 1/(hubble_const/(3.086e+19/(60*60*24*365)))
print("Age of the universe: ", Age, "year")

plt.figure(figsize=(14,10))
plt.plot(distance, velocity, 'o')
plt.plot(distance, fx(distance))
plt.title("[Hubble Diagram]")
plt.xlabel('Distance (MPc)')
plt.ylabel('Velocity (km/s)')
plt.show()


hubble_const_1=50.0
Age_1= 1/(hubble_const_1/(3.086e+19/(60*60*24*365)))
print("Age of the universe: ", Age_1, "year")
err=(Age-Age_1)*100/Age_1
print(err)

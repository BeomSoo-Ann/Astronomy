import astropy.io.fits as fits
import matplotlib.pyplot as plt
import numpy as np

fits_data= fits.open("Elias27_CO.fits")

header= fits_data[0].header
print(header)
ra = header['CRVAL1'] + ( np.arange( header['NAXIS1'] ) - header['CRPIX1'] ) * header['CDELT1']
dec = header['CRVAL2'] + ( np.arange( header['NAXIS2'] ) - header['CRPIX2'] ) * header['CDELT2']
freq = header['CRVAL3'] + ( np.arange( header['NAXIS3'] ) - header['CRPIX3'] ) * header['CDELT3']
freq = freq/1e9

data= fits_data[0].data[0,:,:,:]
data= np.array(data, dtype='f')
#print(data.shape)
xz_data= data[:,:,1000]

plt.figure(figsize=(5,4))
plt.imshow(xz_data, cmap='viridis', origin='lower', aspect='auto',
        extent=[ra[0], ra[-1], freq[0], freq[-1]])

plt.ylabel('Frequency [GHz]') # z axis (frequency)
plt.xlabel('RA (decimal)') # x axis (RA)

plt.show()


#channel map

restfreq= 230.538
c0= 299792
chan= 30
vel= (restfreq-freq[chan])/restfreq*c0

fig= ax= plt.subplot() 
ax.imshow(data[chan, 500:1500, 500:1500], vmin=0, vmax=0.03, cmap='plasma',
        extent=[ra[0], ra[-1], dec[0], dec[-1]])

ax.set_title('{:.2f} km/s'.format(vel))
ax.set_xlabel('RA (decimal)')
ax.set_ylabel('Dec (decimal)')
plt.show()

fig, ax = plt.subplots(4,4,figsize=(15,15)) 
restfreq=230.538
c0 = 299792
chans = np.arange(18,34,1)
vel = ( restfreq-freq[chans] ) / restfreq * c0

k=0
for i in range(0,4):
    for j in range(0,4):
        ax[i,j].imshow(data[chans[k],500:1500,500:1500], vmin=0, vmax=0.03, cmap='plasma', extent=[ra[0],ra[-1],dec[0],dec[-1]])
        ax[i,j].set_xlabel('ra')
        ax[i,j].set_ylabel('dec')
        ax[i,j].set_title('{:.2f} km/s'.format(vel[k]))

        k+=1

plt.tight_layout()
plt.show()
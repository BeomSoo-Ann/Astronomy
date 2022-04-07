import astropy.io.fits as fits
import numpy as np
import matplotlib.pyplot as plt

structure = fits.open('C:/Users/BumLahm/Desktop/Programing/Astronomy_2/swap_lv1_20120606_040010.fits')
data1 = structure[0].data
header1 = structure[0].header


o_image = np.array(data1)
image = np.log(o_image)
max_value = np.percentile(image, 100)
min_value = np.percentile(image, 30)
plt.figure(figsize=(5,5))
plt.imshow(image,cmap='hot',origin='lower',vmax=max_value,vmin=min_value)
plt.show()

arcsec = int(header1['CDELT1'])

#vinus = [394,691], [549,680], [710,677]
#solar_active = [419, 581], [434,581],[440,581]
import astropy.io.fits as fits
import numpy as np
import matplotlib.pyplot as plt

FITS_path = "hst_10089_01_acs_wfc_f814w_sci.fits"
FITS = fits.open(FITS_path)
print(FITS.info())
image = FITS[1].data
header = FITS[1].header
print("Info", header["PHOTMODE"])
print("deg/pixel", header["CD2_2"]) #degree to radian
max_value = np.percentile(image, 99.4)
min_value = np.percentile(image, 70)
image = np.array(image)

plt.figure(figsize=(8,8))
plt.imshow(image, cmap='gray', origin='lower', vmax= max_value, vmin= min_value)
plt.show()

Xp=2796
Yp=2687
Xarr= Xp + np.zeros(3000)
Yarr= Yp + (np.arange(3000) - 1500)

plt.figure(figsize=(8,8))
plt.imshow(image, cmap='gray', origin='lower', vmax= max_value, vmin= min_value)
plt.plot(Xarr, Yarr)
plt.show()

slice_values = image[Yarr, Xp]

plt.figure(figsize=(8,8))
plt.plot(slice_values, Yarr)

plt.xlim(0,1)

plt.xlabel('Intensity', fontsize=15)
plt.ylabel('Pixel', fontsize=15)

V1= 3798
V2= 1724

plt.hlines(V1, 0, 10, color='red', linestyle='--')
plt.hlines(V2, 0, 10, color='red', linestyle='--')
plt.show()

plt.figure(figsize=(8,8))
plt.imshow(image, cmap='gray', origin='lower', vmax= max_value, vmin= min_value)
plt.plot(Xarr, Yarr)

plt.hlines(V1, Xp-500, Xp+500, color='red', linestyle='--')
plt.hlines(V2, Xp-500, Xp+500, color='red', linestyle='--')
plt.show()
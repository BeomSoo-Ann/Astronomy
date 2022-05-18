import astropy.io.fits as fits
import numpy as np
import matplotlib.pyplot as plt

image_data = fits.open(
    '/Users/annbeomsu/projects/Astronomy/d_1/swap_lv1_20120606_000010.fits')
data = image_data[0].data
header = image_data[0].header


# 오류창 제거를 위한 코드
# error --> RuntimeWarning: divide by zero encountered in log
np.seterr(divide='ignore')

# o_image = np.array(data)
# 데이터를 로그 스캐일로 전환
image = np.log(np.array(data))
max_value = np.percentile(image, 100)
min_value = np.percentile(image, 30)

plt.figure(figsize=(8, 8))
plt.imshow(image, cmap='hot', origin='lower', vmax=max_value, vmin=min_value)
plt.show()

arcsec = int(header['CDELT1'])

import numpy as np
import matplotlib.pyplot as plt
import astropy.io.ascii as ascii

file_path= "hlsp_k2sff_k2_lightcurve_206103150-c03_kepler_v1_llc-default-aper.txt"
text= ascii.read(file_path, 'r', data_start=2, delimiter=',')
data= dict(text)

BJD= data['col1']
Flux= data['col2']

BJD= np.array(BJD, dtype='f')
Flux= np.array(Flux, dtype='f')

plt.figure(figsize=(16,8))
plt.plot(BJD, Flux)

plt.title('BJD_Flux', fontsize=10)
plt.xlabel('BJD [day]', fontsize=10)
plt.ylabel('Flux', fontsize=10)
plt.show()

a= 2157.5
b= 2159.0

arrange= np.where((BJD>=a)&(BJD<=b))[0]

x_cut= BJD[arrange]
y_cut= Flux[arrange]

y_min= np.min(y_cut)
wh_min= np.where(y_cut == y_min)[0]
x_min= x_cut[wh_min][0]

print("X axis data:", x_min, "+2453833")
print("Y axis data:", y_min)

plt.figure(figsize=(16,8))
plt.plot(x_cut, y_cut, '-')
plt.plot(x_cut, y_cut, 'o', color='r')
plt.plot(x_min, y_min, '*', markersize='15')

plt.title('BJD_Flux', fontsize=10)
plt.xlabel('BJD [day]', fontsize=10)
plt.ylabel('Flux', fontsize=10)
plt.show()

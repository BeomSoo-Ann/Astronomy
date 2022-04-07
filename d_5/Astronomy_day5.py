import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

file='HD67767_G7_V_K.txt'

f=open(file, 'r')

wavelength= []
flux= []
error = []

n=1

while True:
    line= f.readline()
    columns= line.split('|')

    if not line: break
    if (n==1):
        header= columns[0]
        header= header.replace('#','')
        header= header.split()
        n= n+1
        print("Header : ", header)
    else:
        wavelength.append(columns[0])
        flux.append(columns[1])
        error.append(columns[2])
    
wavelength= np.array(wavelength, dtype='f')
flux= np.array(flux, dtype='f')
error= np.array(error, dtype='f')

def pltmaker(x_data, y_data, xlab, ylab):
    plt.figure(figsize=(16,8))
    plt.plot(x_data, y_data, '-')
    plt.title(xlab+ '-' +ylab, fontsize=10)
    plt.xlabel(xlab,fontsize=10)
    plt.ylabel(ylab,fontsize=10)
    result= plt.show()
    return result

a= 2.2475
b= 2.2483

arange= np.where((wavelength >= a) & (wavelength <= b))[0]
wave_cut= wavelength[arange]
flux_cut= flux[arange]
error_cut= error[arange]

pltmaker(wave_cut, flux_cut, header[0], header[1])

def gauss(x, cont, a, b, c):
    T= (x-b)/c
    y= cont-(a*np.exp(-(T**2/2)))
    return y

x= wave_cut
y= flux_cut

opt,cov = curve_fit(gauss, x, y, p0=[1.09, 0.255, 2.24794, 0.0001])

print("Background spectrum: ", opt[0])
print("Height: ", opt[1])
print("Center: ", opt[2])
print("Width: ", opt[3])

x_fit = np.linspace(a, b, 1000)
y_fit = gauss(x_fit, opt[0], opt[1], opt[2], opt[3])

plt.figure(figsize=(16,8))
plt.errorbar(wave_cut, flux_cut, error_cut, fmt= 'o')
plt.plot(x_fit, y_fit, '-')
plt.title(header[0]+ '-' +header[1], fontsize=10)
plt.xlabel(header[0],fontsize=10)
plt.ylabel(header[1],fontsize=10)
plt.show()
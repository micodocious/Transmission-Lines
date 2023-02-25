import numpy as np

# givens
b = 0.4 * np.pi #beta
vp = 15 * ((10**9)/100) # phase velocity 15 cm/ns
w = 2 * np.pi
# Find Frequency vp = w / b, f=?
f = (b * vp) / w
print(f"The frequency is {f} Hz")
print(f"The frequency is {f*10**(-6)} MHz")
# Find wavelength
# b = w / vp = 2 pi / λ
λ = w / b
print(f"The wavelength is {λ}")


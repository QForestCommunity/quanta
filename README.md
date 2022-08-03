# quanta
A python library simulating optical circuits.

# ***stokes formalism***

The relationship of the Stokes parameters S0, S1, S2, S3 to intensity and polarization ellipse parameters is shown by:

```
S0 = I
S1 = I*p*cos(2φ)cos(2χ)
S2 = I*p*sin(2φ)sin(2χ)
S3 = I*p*sin(2χ)
```

where:
I : intensity of the polarizer
p : degree of polarization
φ : angle between the major axis of the ellipse and the x-axis
χ : ellipticity angle

Stokes vector is given by: 

S = [S0,S1,S2,S3]
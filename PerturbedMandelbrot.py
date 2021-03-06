#!/usr/bin/env python
# Perturbation theory implementation of the Mandelbrot set.

# Copyright (C) 2015 Zechariah Thurman
# GNU GPLv2

import pylab
import matplotlib.pyplot as plt
import numpy as np


def mandelbrot( h, w, maxit=35):
     # Returns an image of the Mandelbrot fractal of size (h,w). Lower the maxit count, the less detail in the
     # set. Increase maxit for more detailed rendering.

    #y,x = ogrid[ -1.4:1.4:h*1j, -2.1:0.8:w*1j ]		# complex plane for set to set on, either ogrid or mgrid work, mgrid is more conventional
    y,x = np.mgrid[ -1.4:1.4:h*1j, -2.1:0.75:w*1j ]
    c = x + y*1j			# initialized c value
    z = c		# first z value intialized to c

    dtime = maxit +  np.zeros(z.shape, dtype=int)		# time of divergence
    an = 0 + 0j		# a initial value, hint came from: http://math.stackexchange.com/questions/939270/perturbation-of-mandelbrot-set-fractal
    bn = 0 + 0j		# b initial value, although these values really don't matter
    cn = 0 + 0j		# c initial value, like at all
    d0 = c		# first d0 initialized to c
    

    for i in xrange(maxit):
        z  = z**2 +  c   #   mandelbrot eqn

    # terms from superfractalthing perturbation implementation
        cn = 2*z*cn + 2*an*bn  # c term
        bn = 2*z*bn + an**2   # b term
        an = 2*z*an + 1	     # a term
        d = an*d0 + bn*d0**2 + cn*d0**3  # delta_n eqn
        dn = 2*z*d + d**2 + d0     # delta_n+1 eqn

    # alternate c initial values for zoom coordinates when that becomes applicable
        # c = -0.74591 + 0.11254j
        # c = -1.764 + 0.01j
        # c = -1.772 + 0.013j
        # c = -1.254024 + 0.046569j
        # c = -0.95 + 0.24387j
        # c = -0.925 + 0.26785j
        # c = -0.1011 + 0.9563j
        # c = 0.001643721971153 - 0.822467633298876j

        yn = z + dn				# perturbed Mandel yn solns
        diverge = ((yn)*(np.conj(yn))).real > 25**25     # who is diverging, term on the right of the inequality determines level of detail
        div_now = diverge & (dtime==maxit)  # who is diverging now
        dtime[div_now] = i                  # note when
        z[diverge] = 2                       # avoid diverging too much
    return dtime

if __name__ == "__main__":
    plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
    pylab.imshow(mandelbrot(500,500), cmap='bone_r')
    pylab.title('The Mandelbrot Viewer')
    pylab.xlabel('Real Values')
    pylab.ylabel('Imaginary Values')
    pylab.show()
import math
import numpy as np


def horizontal() -> np.array:
    """Returns the Stokes matrix when horizontal linearly polarized."""
    return np.asarray([[1, 1, 0, 0]])


def vertical() -> np.array:
    """Returns the Stokes matrix when vertical linearly polarized."""
    return np.asarray([[1, -1, 0, 0]])


def diagonal_positive() -> np.array:
    """Returns the Stokes vector when linearly polarized at +45°"""
    return np.asarray([[1, 0, 1, 0]])


def diagonal_negative() -> np.array:
    """Returns the Stokes vector when linearly polarized at -45°"""
    return np.asarray([[1, 0, -1, 1]])


def polarizer(I, p, psi, chi) -> np.array:
    """Returns the Stokes vector when linear polarized at an intensity of I, 
    p degree of polarization, psi defined as the angle between the major 
    axis of the ellipse and the x-axis and finally chi which is the 
    ellipticity angle i.e, arctan(b/a)
    Args:
        I : intensity of the polarizer
        p : degree of polarization
        psi : angle between the major axis of the ellipse and the x-axis
        chi : ellipticity angle
    """
    psi = (math.pi/180)*psi
    chi = (math.pi/180)*chi
    return np.asarray([[I, I*np.cos(2*psi)*np.cos(2*chi), I*np.sin(2*psi)*np.cos(2*chi), I*np.sin(2*chi)]])

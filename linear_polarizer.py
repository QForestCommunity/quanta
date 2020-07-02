# -*- coding: utf-8 -*-
# pylint: disable=no-member

"""Implementation of linear polarizers using Jones matrices."""

import math
import numpy as np

def horizontal() -> np.array:
    """Returns the Jones matrix for a horizontal linear polarizer."""
    return np.asarray([[1, 0], [0, 0]])

def vertical() -> np.array:
    """Returns the Jones matrix for a horizontal linear polarizer."""
    return np.asarray([[0, 0], [0, 1]])

def diagonal_positive() -> np.array:
    """Returns the Jones matrix for linear polarizer at +45°"""
    return 1/2 * np.asarray([[1, 1], [1, 1]])

def diagonal_negative() -> np.array:
    """Returns the Jones matrix for linear polarizer at -45°"""
    return 1/2 * np.asarray([[1, -1], [-1, 1]])

def polarizer(theta: int = 0) -> np.array:
    """Returns the Jones matrix for a linear polarizer rotated at an angle theta.
    Args:
        theta   :   angle in degreed at which the polarizer is rotated.
    """
    theta = (math.pi/180)*theta
    return np.asarray([[np.cos(theta), np.sin(theta)], [np.sin(theta), -np.cos(theta)]])

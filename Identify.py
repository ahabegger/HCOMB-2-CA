"""
Identify.py
This file is used to identify the type of structure that is being
used given the XYZ coordinates of the atoms in the structure.
"""

import numpy as np

from Preprocessing import get_amino_acid_distances


def identify_structure(xyz):
    """
    identify_structure
    This function is used to identify the type of structure that is
    being used given the XYZ coordinates of the atoms in the structure.
    :param xyz:
    """


    print(xyz)

    # Math Calculations
    sqrt_3_div_2 = np.sqrt(3) / 2
    sqrt_2_div_2 = np.sqrt(2) / 2

    #print(xyz)


def get_movements(xyz):
    """
    get_movements
    This function is used to get the movements of the atoms in the
    structure.
    :param xyz:
    :return: A numpy array of the movements of the atoms in the
    structure.
    """

    movements = np.zeros((xyz.shape[0] - 1, xyz.shape[1]))
    for i in range(len(xyz) - 1):
        movements[i] = xyz[i + 1] - xyz[i]

    return movements


def untilt(movements):




    for movement in movements:
        while not np.any(np.allclose(movement, potential_movements)):


def check_valid_movements(movements):
    """
    check_valid_movements
    This function is used to check if the given movements are valid
    movements.
    :param movements:
    :return: True if the given movements are valid movements, False
    """

    # Math Calculations
    sqrt_3_div_2 = np.sqrt(3) / 2
    sqrt_2_div_2 = np.sqrt(2) / 2

    valid_movements = [
        [1, 0, 0], [-1, 0, 0],
        [0, 1, 0], [0, -1, 0],
        [0, 0, 1], [0, 0, -1],
        [sqrt_3_div_2, 0.5, 0], [-sqrt_3_div_2, 0.5, 0],
        [sqrt_3_div_2, -0.5, 0], [-sqrt_3_div_2, -0.5, 0],
        [sqrt_2_div_2, sqrt_2_div_2, 0], [sqrt_2_div_2, 0, sqrt_2_div_2],
        [0, sqrt_2_div_2, sqrt_2_div_2], [-sqrt_2_div_2, -sqrt_2_div_2, 0],
        [-sqrt_2_div_2, 0, -sqrt_2_div_2], [0, -sqrt_2_div_2, -sqrt_2_div_2],
        [sqrt_2_div_2, -sqrt_2_div_2, 0], [sqrt_2_div_2, 0, -sqrt_2_div_2],
        [0, sqrt_2_div_2, -sqrt_2_div_2], [-sqrt_2_div_2, sqrt_2_div_2, 0],
        [-sqrt_2_div_2, 0, sqrt_2_div_2], [0, -sqrt_2_div_2, sqrt_2_div_2]
    ]

    for movement in movements:
        if not np.any(np.allclose(movement, valid_movements)):
            return False

    return True

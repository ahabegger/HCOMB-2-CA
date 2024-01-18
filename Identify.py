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



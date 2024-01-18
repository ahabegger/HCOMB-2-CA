import pandas as pd
import numpy as np

"""
Identify.py
This file is used to identify the type of structure that is being
used given the XYZ coordinates of the atoms in the structure.
"""


def valid_xyz_csv(xyz_csv):
    """
    valid_xyz_csv
    This function is used to check if the given csv file is a valid
    xyz csv file.
    """

    # Check if xyz_csv is a csv file
    if xyz_csv[-4:] != '.csv':
        print('Error: The file given is not a csv file.')
        return False

    # Create a dataframe from the csv file
    try:
        df = pd.read_csv(xyz_csv)
        if df.shape[1] == 3:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def get_xyz(file):
    """
    get_xyz
    This function is used to get the XYZ coordinates of the atoms
    in the structure.
    """

    df = pd.read_csv(file)
    xyz = df.values.tolist()
    xyz = np.array(xyz)

    return xyz


def identify_structure(xyz):
    """
    identify_structure
    This function is used to identify the type of structure that is
    being used given the XYZ coordinates of the atoms in the structure.
    """
    pass

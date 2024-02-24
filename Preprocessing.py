"""
Preprocessing
This file is used to preprocess the data.
"""

import numpy as np
import pandas as pd


def valid_xyz_csv(xyz_csv):
    """
    valid_xyz_csv
    This function is used to check if the given csv file is a valid
    xyz csv file.
    :param xyz_csv:
    :return: True if the csv file is a valid xyz csv file, False
    otherwise.
    """

    # Check if xyz_csv is a csv file
    if xyz_csv[-4:] != '.csv':
        print('Error: The file given is not a csv file.')
        return False

    # Create a dataframe from the csv file
    try:
        df = pd.read_csv(xyz_csv)
        if 'X' in df.columns and 'Y' in df.columns and 'Z' in df.columns:
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
    :param file:
    :return: A numpy array of the XYZ coordinates of the atoms in
    the structure.
    """

    df = pd.read_csv(file)
    xyz_df = df[['X', 'Y', 'Z']].copy()
    xyz = xyz_df.values.tolist()
    xyz = np.array(xyz)

    return xyz


def get_amino_acid_distances(xyz):
    """
    get_amino_acid_distances
    This function is used to get the distances between each amino acid
    in the structure.
    :param xyz:
    :return: A numpy array of the distances between each amino acid in
    the structure.
    """

    amino_acid_distances = []
    for i in range(len(xyz) - 1):
        amino_acid_distances.append(np.linalg.norm(xyz[i] - xyz[i + 1]))

    return np.array(amino_acid_distances)


def check_normalize_xyz(xyz):
    """
    check_normalize_xyz
    This function is used to normalize the XYZ coordinates of the atoms
    in the structure.
    :param xyz:
    :return: A numpy array of the normalized XYZ coordinates of the atoms
    """

    amino_acid_distances = get_amino_acid_distances(xyz)
    std = amino_acid_distances.std()

    if std > 0.05:
        print('Error: The structure is not a valid structure.')
        print('The standard deviation between movements is too large.')
        exit(1)

    # Normalize the xyz coordinates
    average = amino_acid_distances.mean()
    xyz = xyz / average

    if xyz[0].max() > 0.1:
        print('Error: The structure is not a valid structure.')
        print('Structure must start at the origin.')
        exit(1)

    return xyz


def normalize_xyz(xyz):
    """
    normalize_xyz
    This function is used to normalize the XYZ coordinates of the atoms
    in the structure.
    :param xyz:
    :return: A numpy array of the normalized XYZ coordinates of the atoms
    """

    amino_acid_distances = get_amino_acid_distances(xyz)

    # Normalize the xyz coordinates
    average = amino_acid_distances.mean()
    xyz = xyz / average

    # for each row subtract the first row
    for i in range(len(xyz)):
        xyz[i] = xyz[i] - xyz[0]

    return xyz.flatten()


def get_acids(xyz_csv):
    """
    get_acids
    This function is used to get the amino acids in the structure.
    :param xyz_csv:
    :return: A numpy array of the amino acids in the structure.
    """

    df = pd.read_csv(xyz_csv)
    acids = df['Amino Acid'].values.tolist()
    acids = np.array(acids)

    return acids


def get_input_value(acids, moves):
    """
    get_input_value
    This function is used to get the input value for the neural network.
    :param acids:
    :param moves:
    :return: inputs
    """

    inputs = []
    for i in range(len(moves)):
        inputs.append(acids[i])
        inputs.append(moves[i])
    inputs.append(acids[-1])

    return inputs

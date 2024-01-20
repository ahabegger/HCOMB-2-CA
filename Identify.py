"""
Identify.py
This file is used to identify the type of structure that is being
used given the XYZ coordinates of the atoms in the structure.
"""

import numpy as np


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
    for i in range(360):
        print(i)
        for j in range(360):
            for k in range(360):
                rotated_movements = rotate_movements(movements, i, j, k)
                if check_valid_movements(rotated_movements):
                    return rotated_movements

    print("Error: Unable to untilt the structure.")
    exit(1)


def rotate_movements(movements, degree_x, degree_y, degree_z):
    # Convert degrees to radians
    angles_rad_x = np.radians(degree_x)
    angles_rad_y = np.radians(degree_y)
    angles_rad_z = np.radians(degree_z)

    # Compute sin and cos for each angle
    sin_x, cos_x = np.sin(angles_rad_x), np.cos(angles_rad_x)
    sin_y, cos_y = np.sin(angles_rad_y), np.cos(angles_rad_y)
    sin_z, cos_z = np.sin(angles_rad_z), np.cos(angles_rad_z)

    # Directly compute the combined rotation matrix
    rotation_matrix = np.array([
        [cos_y * cos_z, cos_z * sin_x * sin_y - cos_x * sin_z, sin_x * sin_z + cos_x * cos_z * sin_y],
        [cos_y * sin_z, cos_x * cos_z + sin_x * sin_y * sin_z, cos_x * sin_y * sin_z - cos_z * sin_x],
        [-sin_y, cos_y * sin_x, cos_x * cos_y]
    ])

    # Apply the rotation to the movements
    changed_movements = np.dot(movements, rotation_matrix)

    return changed_movements


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

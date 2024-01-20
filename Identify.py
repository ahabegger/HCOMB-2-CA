"""
Identify.py
This file is used to identify the type of structure that is being
used given the XYZ coordinates of the atoms in the structure.
"""

import numpy as np


def close_to_any(main_vector, set_of_vectors, threshold=0.15):

    for vector in set_of_vectors:
        vector = np.array(vector)
        main_vector = np.array(main_vector)
        distance = np.linalg.norm(main_vector - vector)
        if distance < threshold:
            return True

    return False


def identify(xyz):
    """
    identify
    This function is used to identify the type of structure that is
    being used given the XYZ coordinates of the atoms in the
    structure.
    :param xyz:
    :return: The type of structure that is being used.
    """

    # Get the movements of the atoms in the structure
    movements = get_movements(xyz)

    # Get the distance between each movement
    distances = set()
    for move1 in movements:
        for move2 in movements:
            distance = np.linalg.norm(move1 - move2)
            distances.add(distance)
    
    print(distances)

    return None


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


def untilt(xyz, structure_code):
    """
    untilt
    This function is used to untilt the structure.
    :param xyz:
    :param structure_code:
    :return: The untilted structure.
    """

    # Get the movements of the atoms in the structure
    get_movements(xyz)


    # Get the structure information
    structure_name, potential_movements = get_structure_info(structure_code)

    print('Structure Name: ' + structure_name)
    print('Structure Code: ' + str(structure_code))
    print('Movements: ' + str(movements))
    print('Potential Movements: ' + str(potential_movements))

    return None


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


def get_structure_info(num_moves):
    """
    Get the name and movements for a given number of moves.
    :param num_moves:
    :return: structure_name, movements
    """

    # Define Math Calculations
    sqrt_3_div_2 = np.sqrt(3) / 2
    sqrt_2_div_2 = np.sqrt(2) / 2

    # Return Structure Name and Movements
    if num_moves == 4:
        return ("SQUARE TILING",
                [
                    [1, 0, 0],
                    [-1, 0, 0],
                    [0, 1, 0],
                    [0, -1, 0]
                ])
    elif num_moves == 6:
        return ("CUBIC HONEYCOMB",
                [
                    [1, 0, 0], [-1, 0, 0],
                    [0, 1, 0], [0, -1, 0],
                    [0, 0, 1], [0, 0, -1]
                ])
    elif num_moves == 8:
        return ("TRIANGULAR PRISMATIC HONEYCOMB",
                [
                    [sqrt_3_div_2, 0.5, 0], [-sqrt_3_div_2, 0.5, 0],
                    [0, 1, 0], [sqrt_3_div_2, -0.5, 0],
                    [-sqrt_3_div_2, -0.5, 0], [0, -1, 0],
                    [0, 0, 1], [0, 0, -1]
                ])
    elif num_moves == 12:
        return ("TETRAHEDRAL-OCTAHEDRAL HONEYCOMB",
                [
                    [sqrt_2_div_2, sqrt_2_div_2, 0], [sqrt_2_div_2, 0, sqrt_2_div_2],
                    [0, sqrt_2_div_2, sqrt_2_div_2], [-sqrt_2_div_2, -sqrt_2_div_2, 0],
                    [-sqrt_2_div_2, 0, -sqrt_2_div_2], [0, -sqrt_2_div_2, -sqrt_2_div_2],
                    [sqrt_2_div_2, -sqrt_2_div_2, 0], [sqrt_2_div_2, 0, -sqrt_2_div_2],
                    [0, sqrt_2_div_2, -sqrt_2_div_2], [-sqrt_2_div_2, sqrt_2_div_2, 0],
                    [-sqrt_2_div_2, 0, sqrt_2_div_2], [0, -sqrt_2_div_2, sqrt_2_div_2]
                ])


def check_valid_movements(movements, potential_movements):
    """
    check_valid_movements
    This function is used to check if the given movements are valid
    movements.
    :param movements:
    :return: True if the given movements are valid movements, False
    """

    for movement in movements:
        if not np.any(np.allclose(movement, potential_movements)):
            return False

    return True

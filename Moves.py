"""
Moves.py
This file is used to get the moves from the movement vectors.
"""

import numpy as np
from Identify import get_movements


def get_moves(xyz, structure_code):
    """
    get_moves
    This function is used to get the moves from the movement vectors.
    :param xyz:
    :param structure_code:
    :return:
    """

    movement_vectors = get_movements(xyz)

    if structure_code == 4:
        return get_moves_4(movement_vectors)
    elif structure_code == 6:
        return get_moves_6(movement_vectors)
    elif structure_code == 8:
        return get_moves_8(movement_vectors)
    elif structure_code == 12:
        return get_moves_12(movement_vectors)
    else:
        print('Error: Invalid Structure Code.')
        exit(1)


def get_moves_4(movement_vectors):
    """
    get_moves_4
    This function is used to get the moves from the movement vectors
    for Square Tiling Structure Simplifications.
    :param movement_vectors:
    :return: move_set
    """

    moves = []
    potential_moves = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, -0]]

    for vector in movement_vectors:
        vector = np.array(vector, dtype=np.float16)
        if is_close(vector, [1, 0, 0]):
            moves.append(0)
        elif is_close(vector, [-1, 0, 0]):
            moves.append(1)
        elif is_close(vector, [0, 1, 0]):
            moves.append(2)
        elif is_close(vector, [0, -1, 0]):
            moves.append(3)
        else:
            print('Error: Invalid Movement Vector: ' + str(vector) + '.')
            exit(1)

    # Check if the moves are valid
    if not is_valid_moves(moves, potential_moves):
        print('Error: Invalid Move Set: ' + str(moves) + '.')
        exit(1)

    return moves


def get_moves_6(movement_vectors):
    """
    get_moves_6
    This function is used to get the moves from the movement vectors
    for Cubic Honeycomb Structure Simplifications.
    :param movement_vectors:
    :return: move_set
    """

    moves = []
    potential_moves = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, -0], [0, 0, 1], [0, 0, -1]]

    for vector in movement_vectors:
        vector = np.array(vector, dtype=np.float16)
        if is_close(vector, [1, 0, 0]):
            moves.append(0)
        elif is_close(vector, [-1, 0, 0]):
            moves.append(1)
        elif is_close(vector, [0, 1, 0]):
            moves.append(2)
        elif is_close(vector, [0, -1, 0]):
            moves.append(3)
        elif is_close(vector, [0, 0, 1]):
            moves.append(4)
        elif is_close(vector, [0, 0, -1]):
            moves.append(5)
        else:
            print('Error: Invalid Movement Vector: ' + str(vector) + '.')
            exit(1)

    # Check if the moves are valid
    if not is_valid_moves(moves, potential_moves):
        print('Error: Invalid Move Set: ' + str(moves) + '.')
        exit(1)

    return moves


def get_moves_8(movement_vectors):
    """
    get_moves_8
    This function is used to get the moves from the movement vectors
    for Triangular Prismatic Honeycomb Structure Simplifications.
    :param movement_vectors:
    :return: move_set
    """

    moves = []
    sqrt_3_div_2 = np.sqrt(3) / 2
    potential_moves = [
        [sqrt_3_div_2, 0.5, 0], [-sqrt_3_div_2, 0.5, 0],
        [0, 1, 0], [sqrt_3_div_2, -0.5, 0],
        [-sqrt_3_div_2, -0.5, 0], [0, -1, 0],
        [0, 0, 1], [0, 0, -1]]

    for vector in movement_vectors:
        vector = np.array(vector, dtype=np.float16)
        if is_close(vector, [sqrt_3_div_2, 0.5, 0]):
            moves.append(0)
        elif is_close(vector, [-sqrt_3_div_2, 0.5, 0]):
            moves.append(1)
        elif is_close(vector, [0, 1, 0]):
            moves.append(2)
        elif is_close(vector, [sqrt_3_div_2, -0.5, 0]):
            moves.append(3)
        elif is_close(vector, [-sqrt_3_div_2, -0.5, 0]):
            moves.append(4)
        elif is_close(vector, [0, -1, 0]):
            moves.append(5)
        elif is_close(vector, [0, 0, 1]):
            moves.append(6)
        elif is_close(vector, [0, 0, -1]):
            moves.append(7)
        else:
            print('Error: Invalid Movement Vector: ' + str(vector) + '.')
            exit(1)

    # Check if the moves are valid
    if not is_valid_moves(moves, potential_moves):
        print('Error: Invalid Move Set: ' + str(moves) + '.')
        exit(1)

    return moves


def get_moves_12(movement_vectors):
    """
    get_moves_12
    This function is used to get the moves from the movement vectors
    for Tetrahedral-Octahedral Honeycomb Structure Simplifications.
    :param movement_vectors:
    :return: move_set
    """

    moves = []
    sqrt_2_div_2 = np.sqrt(2) / 2
    potential_moves = [
        [sqrt_2_div_2, sqrt_2_div_2, 0], [sqrt_2_div_2, 0, sqrt_2_div_2],
        [0, sqrt_2_div_2, sqrt_2_div_2], [-sqrt_2_div_2, -sqrt_2_div_2, 0],
        [-sqrt_2_div_2, 0, -sqrt_2_div_2], [0, -sqrt_2_div_2, -sqrt_2_div_2],
        [sqrt_2_div_2, -sqrt_2_div_2, 0], [sqrt_2_div_2, 0, -sqrt_2_div_2],
        [0, sqrt_2_div_2, -sqrt_2_div_2], [-sqrt_2_div_2, sqrt_2_div_2, 0],
        [-sqrt_2_div_2, 0, sqrt_2_div_2], [0, -sqrt_2_div_2, sqrt_2_div_2]
    ]

    for vector in movement_vectors:
        vector = np.array(vector, dtype=np.float16)
        if is_close(vector, [sqrt_2_div_2, sqrt_2_div_2, 0]):
            moves.append(0)
        elif is_close(vector, [sqrt_2_div_2, 0, sqrt_2_div_2]):
            moves.append(1)
        elif is_close(vector, [0, sqrt_2_div_2, sqrt_2_div_2]):
            moves.append(2)
        elif is_close(vector, [-sqrt_2_div_2, -sqrt_2_div_2, 0]):
            moves.append(3)
        elif is_close(vector, [-sqrt_2_div_2, 0, -sqrt_2_div_2]):
            moves.append(4)
        elif is_close(vector, [0, -sqrt_2_div_2, -sqrt_2_div_2]):
            moves.append(5)
        elif is_close(vector, [sqrt_2_div_2, -sqrt_2_div_2, 0]):
            moves.append(6)
        elif is_close(vector, [sqrt_2_div_2, 0, -sqrt_2_div_2]):
            moves.append(7)
        elif is_close(vector, [0, sqrt_2_div_2, -sqrt_2_div_2]):
            moves.append(8)
        elif is_close(vector, [-sqrt_2_div_2, sqrt_2_div_2, 0]):
            moves.append(9)
        elif is_close(vector, [-sqrt_2_div_2, 0, sqrt_2_div_2]):
            moves.append(10)
        elif is_close(vector, [0, -sqrt_2_div_2, sqrt_2_div_2]):
            moves.append(11)
        else:
            print('Error: Invalid Movement Vector: ' + str(vector) + '.')
            exit(1)

    # Check if the moves are valid
    if not is_valid_moves(moves, potential_moves):
        print('Error: Invalid Move Set.')
        exit(1)

    return moves


def is_valid_moves(moves, possible_movements):
    """
    Check if a set of moves is valid based on the possible movements
    :param moves:
    :param possible_movements:
    :return: validity
    """

    # Ensure moves is a NumPy array
    moves = np.array(moves, dtype=int)

    # Check if possible_movements is a list of lists or a 2D NumPy array
    if isinstance(possible_movements, list):
        possible_movements = np.array(possible_movements)

    # Initialize the xyz array with the origin and correct size
    xyz = np.zeros((len(moves) + 1, 3), dtype=np.float16)

    # Efficiently compute the cumulative sum of movements
    xyz[1:] = np.cumsum(possible_movements[moves], axis=0, dtype=np.float16)

    # Check if any of the xyz coordinates are within 0.2 of each other
    for i, point in enumerate(xyz):
        distances = np.linalg.norm(xyz - point, axis=1)
        distances[i] = np.inf  # Ignore the distance of the point to itself
        if np.any(distances < 0.2):
            return False

    return True


def is_close(vector1, vector2, threshold=0.15):
    """
    is_close
    This function is used to determine if two vectors are close to each
    other.
    :param vector1:
    :param vector2:
    :param threshold:
    :return: True if the vectors are close to each other, False
    otherwise.
    """

    vector1 = np.array(vector1)
    vector2 = np.array(vector2)
    distance = np.linalg.norm(vector1 - vector2)
    if distance < threshold:
        return True
    else:
        return False

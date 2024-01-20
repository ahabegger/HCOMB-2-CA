"""
Identify.py
This file is used to identify the type of structure that is being used.
"""

import numpy as np


def identify(xyz):
    """
    identify
    This function is used to identify the type of structure that is
    being used given the XYZ coordinates of the atoms in the
    structure.
    :param xyz:
    :return: The type of structure that is being used.
    """

    movements = get_movements(xyz)

    movement_set = []
    for move in movements:
        move = move.tolist()
        if not close_to_any(move, movement_set):
            movement_set.append(move)
        neg_move = [-move[0], -move[1], -move[2]]
        if not close_to_any(neg_move, movement_set):
            movement_set.append(neg_move)

    distance_counter = {
        0.0: 0,
        1.0: 0,
        1.4: 0,
        1.7: 0,
        2.0: 0
    }

    for move in movement_set:
        for move2 in movement_set:
            move = np.array(move)
            move2 = np.array(move2)
            distance = np.linalg.norm(move - move2)

            if distance < 0.5:
                distance_counter[0.0] += 1
            elif distance < 1.2:
                distance_counter[1.0] += 1
            elif distance < 1.55:
                distance_counter[1.4] += 1
            elif distance < 1.85:
                distance_counter[1.7] += 1
            else:
                distance_counter[2.0] += 1

    if distance_counter[1.0] == 0 and distance_counter[1.7] == 0:
        if len(movement_set) > 4:
            return 6, "CUBIC HONEYCOMB"
        else:
            return 4, "SQUARE TILING"
    else:
        if len(movement_set) > 8:
            return 12, "TETRAHEDRAL-OCTAHEDRAL HONEYCOMB"
        else:
            return 8, "TRIANGULAR PRISMATIC HONEYCOMB"


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


def close_to_any(main_vector, set_of_vectors, threshold=0.15):
    """
    close_to_any
    This function is used to determine if a vector is close to any
    vector in a set of vectors.
    :param main_vector:
    :param set_of_vectors:
    :param threshold:
    :return: True if the vector is close to any vector in the set of
    vectors, False otherwise.
    """

    for vector in set_of_vectors:
        vector = np.array(vector)
        main_vector = np.array(main_vector)
        distance = np.linalg.norm(main_vector - vector)
        if distance < threshold:
            return True

    return False

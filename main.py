"""
main.py
This file is used to run the program.
"""

import argparse
import subprocess

from Identify import identify
from Preprocessing import valid_xyz_csv, get_xyz, check_normalize_xyz, get_acids, convert_to_pdb


def execute(csv_file, output_csv_file):
    """
    execute
    This function is used to execute the program.
    :param output_csv_file:
    :param csv_file:
    """

    xyz = get_xyz(csv_file)
    acids = get_acids(csv_file)
    xyz = check_normalize_xyz(xyz)
    structure_code, structure_name = identify(xyz)

    print('Structure Identified as ' + structure_name)
    print('Structure Code: ' + str(structure_code))

    pdb_file = convert_to_pdb(xyz, acids, structure_name)

    output = subprocess.run(['./pulchra304/bin/win32/pulchra', pdb_file])
    print(output)

    

    """ moves = get_moves(xyz, structure_code)

    print('Moves: ' + str(moves))

    input_value = get_input_value(acids, moves)

    print('Input Value: ' + str(input_value))"""

    # https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2692024/
    # PULCHRA

    """if output_csv_file is not None:
        output_xyz = get_xyz(output_csv_file)
        output_xyz = normalize_xyz(output_xyz)
        print('Output Value: ' + str(output_xyz))
    """


def argument_parser():
    """
    argument_parser
    This function is used to parse the arguments.
    :return: The arguments.
    """
    parser = argparse.ArgumentParser(description='This program is used to convert a structure simplification into a '
                                                 'all atom structure.')

    # Add Arguments
    parser.add_argument('csv', metavar='csv', type=str, nargs=1, help='The csv file that contains the xyz coordinates '
                                                                      'of structure simplification.')
    parser.add_argument('-a', '--add-output', metavar='FILENAME', type=str, help='Add the output to the ML dataset.')

    # Execute the parse_args() method
    user_inputs = parser.parse_args()

    return user_inputs


if __name__ == '__main__':
    # Get Arguments
    args = argument_parser()

    xyz_csv = args.csv[0]
    output_csv = args.add_output

    if xyz_csv is None:
        print('Error: No csv file was given.')
        exit(1)

    xyz_csv = xyz_csv.strip().replace('\\\\', '\\')

    if valid_xyz_csv(xyz_csv) is False:
        print('Error: The csv file given is not a valid xyz csv file.')
        exit(1)

    if output_csv is not None:
        output_csv = output_csv.strip().replace('\\\\', '\\')
        if valid_xyz_csv(output_csv) is False:
            print('Error: The csv file given is not a valid xyz csv file.')
            exit(1)

    # Execute Program
    execute(xyz_csv, output_csv)

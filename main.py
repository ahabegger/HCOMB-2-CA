import argparse
from Identify import valid_xyz_csv, get_xyz, identify_structure

'''
main.py
This file is used to run the program.
'''


def execute(csv_file):
    """
    execute
    This function is used to execute the program.
    """

    xyz = get_xyz(csv_file)
    structure_type = identify_structure(xyz)


def argument_parser():
    """
    argument_parser
    This function is used to parse the arguments.
    """
    parser = argparse.ArgumentParser(description='This program is used to convert a structure simplification into a '
                                                 'all atom structure.')

    # Add Arguments
    parser.add_argument('csv', metavar='csv', type=str, nargs=1, help='The csv file that contains the xyz coordinates '
                                                                      'of structure simplification.')

    # Execute the parse_args() method
    user_inputs = parser.parse_args()

    return user_inputs


if __name__ == '__main__':
    # Get Arguments
    args = argument_parser()

    xyz_csv = args.csv

    if xyz_csv is None:
        print('Error: No csv file was given.')
        exit(1)

    if valid_xyz_csv(xyz_csv) is False:
        print('Error: The csv file given is not a valid xyz csv file.')
        exit(1)

    # Execute Program
    execute(xyz_csv)

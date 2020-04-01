import sys
import os

current_work_directory = os.getcwd()    # Return a string representing the current working directory.
print('Current work directory: {}'.format(current_work_directory))
# Make sure it's an absolute path.
abs_work_directory = os.path.abspath(current_work_directory)
print('Current work directory (full path): {}'.format(abs_work_directory))
print()

filename = 'NYT-bestsellers.txt'
# Check whether file exists.
if not os.path.isfile(filename):
    # Stop with leaving a note to the user.
    print('It seems file "{}" not exists in directory: "{}"'.format(filename, current_work_directory))
    sys.exit(1)

# File exists, go on!
with open(filename, 'r') as file:
    pass
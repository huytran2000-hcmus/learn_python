'''Get files in directory

    This module provides functions that generate a list file names recursively in a directory
    When it be runned as a script:
        - First argument is root directory(default current directory)
        - Second and following arguments are file extensions(excludes dot)
         that you want to be included(default includes all)
    This exports:
        Functions:
            list_files: generate all file names in a directory.
'''
import os
from typing import Generator, Iterable


def list_files(path: str = '', extensions: Iterable[str] = None)-> Generator:
    '''Return a generator of all file names under the specified path.

    :param path: relative or full root directory to run on
    :type path: str
    :param extensions: file extensions(dot excluded) to include, if none include all
    :type extensions: Iterable[str]
    :returns: Nothing
    :rtype: Generator[str]
    '''
    for root, _, files in os.walk(path):
        for file in files:
            if not extensions:
                yield os.path.join(root, file)
            else:
                for ext in extensions:
                    if file.endswith('.' + ext):
                        yield os.path.join(root, file)
                        break

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 3:
        files = list_files(sys.argv[1], sys.argv[2:])
    elif len(sys.argv) == 2:
        files = list_files(sys.argv[1])
    else:
        files = list_files(os.getcwd())

    for file in files:
        print(file)

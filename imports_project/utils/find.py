from .file_operations import save_to_file, read_file


def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i
        raise NotFoundError(f'{expected} not found in provided iterable. ')


class NotFoundError:
    pass


print(__name__)
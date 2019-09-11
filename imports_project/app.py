# import file_operations
from utils.file_operations import save_to_file, read_file
from utils.find import find_in


save_to_file('Tanima Ranjan', 'data.txt')

print(read_file('data.txt'))


print(__name__)
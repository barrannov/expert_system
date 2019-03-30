import sys

from src.new_validation import validation
from src.new_solution import start_solution
from src.read_file import read_buffer

if __name__ == '__main__':

    if (len(sys.argv) != 2):
        raise Exception("usage: python3 main.py file_name")

    read_buffer = read_buffer(sys.argv[1])
    validated = validation(read_buffer)
    facts = start_solution(validated)
    for fact in validated['unknown_vars']:
        print(f'{fact} : {facts.get(fact)}')

import sys
from src.read_file import *
from src.validation import *
from src.new_solution import start_solution
string_usage = "Usage: python3 main.py file_name"


if __name__ == '__main__':

    # if (len(sys.argv) != 2):
    #     error_exit(string_usage)
    # read_buffer = read_file(sys.argv[1])
    read_buffer = read_file('test/my_test')
    dicti = validation(read_buffer)
    facts, unknown_facts = start_solution(dicti)
    for fact in unknown_facts:
        print(f'{fact} : {facts.get(fact)}')

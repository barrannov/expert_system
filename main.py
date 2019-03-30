from src.read_file import *
from src.new_validation import validation
from src.new_solution import start_solution
string_usage = "Usage: python3 main.py file_name"

if __name__ == '__main__':

    if (len(sys.argv) != 2):
        raise Exception(string_usage)

    read_buffer = read_file(sys.argv[1])
    dicti = validation(read_buffer)
    print(dicti)
    facts = start_solution(dicti)
    for fact in dicti['unknown_vars']:
        print(f'{fact} : {facts.get(fact)}')

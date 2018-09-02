import sys
from src.read_file import *
from src.error_exit import *
from src.validation import *
from src.parser import solve_condition
from src.solve_recursion import solve
string_usage = "Usage: python3 main.py file_name"


if __name__ == '__main__':

    # if (len(sys.argv) != 2):
    #     error_exit(string_usage)
    # read_buffer = read_file(sys.argv[1])
    read_buffer = read_file('test/simple')
    dicti = validation(read_buffer)
    # dicti['conditions'] = _prepare_conditions(dicti['conditions'])
    # for cond in dicti['conditions']:
    solve(dicti)
    print('')
    # logic_exp = 'True => True'.split()
    # res = solve_condition(conditon=logic_exp, data=dicti)
    # print(res)
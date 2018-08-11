import sys
from src.read_file import *
from src.error_exit import *
from src.validation import *
string_usage = "Usage: python3 main.py file_name"


if (len(sys.argv) != 2):
    error_exit(string_usage)
read_buffer = read_file(sys.argv[1])
validation_buffer = validation(read_buffer)
# buffer_after_convert = 
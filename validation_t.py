import sys
from os import listdir
from os.path import isfile, join

from src.read_file import *
from src.read_file import *
from src.new_validation import *

GOOD_FILES = 'test/validation/good_files/'
BAD_FILES1 = 'test/validation/bad_files/'
BAD_FILES2 = 'test/validation/bad_files/rules/'
BAD_FILES3 = 'test/validation/bad_files/brackets/'

DEBUG = False
FAIL = '\033[91m'
SUCCESS = '\033[92m'
END = '\033[0m'

def test_bad_files(filelist, path):
	i = 0
	for f in filelist:
		i += 1
		try:
			read_buffer = read_file(f'{path}{f}')
			parsed_data = validation(read_buffer)

			result(i, False, None, f'{path}{f}')
		except Exception as e:
			result(i, True, e, f'{path}{f}')



def test_good_files(filelist, path):
	i = 0
	for f in filelist:
		i += 1
		try:
			read_buffer = read_file(f'{path}{f}')
			parsed_data = validation(read_buffer)

			result(i, True, None, f'{path}{f}')
		except Exception as e:
			result(i, False, e, f'{path}{f}')
			




def result(test_num=0, success=False, e=None, file=''):

	# if turn ON DEBUG flag show more info
	if DEBUG :
		print('\nFILE: ' + file)
		if e:
			print(e)

	# if test pass successfully
	if success == True:
		print(SUCCESS + f'Test {test_num} SUCCESS' + END)
	# if test FAIL
	else :
		print(FAIL + f'Test {test_num} FAIL' + END)	
			




if __name__ == '__main__':

	if (len(sys.argv) == 2 and sys.argv[1] == '-d'):
		DEBUG = True

	bad_files1 = [f for f in listdir(BAD_FILES1) if isfile(join(BAD_FILES1, f))]
	bad_files2 = [f for f in listdir(BAD_FILES2) if isfile(join(BAD_FILES2, f))]
	bad_files3 = [f for f in listdir(BAD_FILES3) if isfile(join(BAD_FILES3, f))]

	print("\n\nsyntax error common")
	test_bad_files(bad_files1, BAD_FILES1)

	print("\n\nsyntax error rules")
	test_bad_files(bad_files2, BAD_FILES2)
	
	print("\n\nsyntax error brackets")
	test_bad_files(bad_files3, BAD_FILES3)

	good_files = [f for f in listdir(GOOD_FILES) if isfile(join(GOOD_FILES, f))]
	print("\n\nTest good files")
	test_good_files(good_files, GOOD_FILES)
	files_count = len(bad_files1) + len(bad_files2) + len(bad_files3) + len(good_files)
	print(f"\nTESTED ON {files_count} files")




	
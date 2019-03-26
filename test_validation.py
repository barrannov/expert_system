import sys

from src.read_file import *
from src.read_file import *
from src.new_validation import *

INVALID_TESTS = 'test/validation/'
DEBUG = False
FAIL = '\033[91m'
SUCCESS = '\033[92m'
END = '\033[0m'

def test_not_valid_1():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}all_var_known')
		parsed_data = validation(read_buffer)

		result(1, False, None, 'all_var_known')
	except Exception as e:
		result(1, True, e, 'all_var_known')



def test_not_valid_2():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}double_var')
		parsed_data = validation(read_buffer)

		result(2, False, None, 'double_var')
	except Exception as e:
		result(2, True, e, 'double_var')




def test_not_valid_3():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}if_and_only_if_many')
		parsed_data = validation(read_buffer)

		result(3, False, None, 'if_and_only_if_many')
	except Exception as e:
		result(3, True, e, 'if_and_only_if_many')




def test_not_valid_4():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}many_implies')
		parsed_data = validation(read_buffer)

		result(4, False, None, 'many_implies')
	except Exception as e:
		result(4, True, e, 'many_implies')




def test_not_valid_5():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}text')
		parsed_data = validation(read_buffer)

		result(5, False, None, 'text')
	except Exception as e:
		result(5, True, e, 'text')




def test_not_valid_6():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}too_big_count_unknow_line')
		parsed_data = validation(read_buffer)

		result(6, False, None, 'too_big_count_unknow_line')
	except Exception as e:
		result(6, True, e, 'too_big_count_unknow_line')




def test_not_valid_7():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}too_small_file')
		parsed_data = validation(read_buffer)

		result(7, False, None, 'too_small_file')
	except Exception as e:
		result(7, True, e, 'too_small_file')




def test_not_valid_8():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}wrong_position_for_uknow_var')
		parsed_data = validation(read_buffer)

		result(8, False, None, 'wrong_position_for_uknow_var')
	except Exception as e:
		result(8, True, e, 'wrong_position_for_uknow_var')




def test_not_valid_9():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}brackets/test_1')
		parsed_data = validation(read_buffer)

		result(9, False, None, 'brackets/test_1')
	except Exception as e:
		result(9, True, e, 'brackets/test_1')



def test_not_valid_10():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}brackets/test_2')
		parsed_data = validation(read_buffer)

		result(10, False, None, 'brackets/test_2')
	except Exception as e:
		result(10, True, e, 'brackets/test_2')


def test_not_valid_11():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}brackets/test_3')
		parsed_data = validation(read_buffer)

		result(11, False, None, 'brackets/test_3')
	except Exception as e:
		result(11, True, e, 'brackets/test_3')



def test_not_valid_12():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}brackets/test_4')
		parsed_data = validation(read_buffer)

		result(12, False, None, 'brackets/test_4')
	except Exception as e:
		result(12, True, e, 'brackets/test_4')



def test_not_valid_13():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}brackets/test_5')
		parsed_data = validation(read_buffer)

		result(13, False, None, 'brackets/test_5')
	except Exception as e:
		result(13, True, e, 'brackets/test_5')



def test_not_valid_14():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}brackets/test_6')
		parsed_data = validation(read_buffer)

		result(14, False, None, 'brackets/test_6')
	except Exception as e:
		result(14, True, e, 'brackets/test_6')



def test_not_valid_15():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}brackets/test_7')
		parsed_data = validation(read_buffer)

		result(15, False, None, 'brackets/test_7')
	except Exception as e:
		result(15, True, e, 'brackets/test_7')



def test_not_valid_16():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}brackets/test_8')
		parsed_data = validation(read_buffer)

		result(16, False, None, 'brackets/test_8')
	except Exception as e:
		result(16, True, e, 'brackets/test_8')




def test_not_valid_17():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}brackets/test_9')
		parsed_data = validation(read_buffer)

		result(17, False, None, 'brackets/test_9')
	except Exception as e:
		result(17, True, e, 'brackets/test_9')



def test_not_valid_18():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}brackets/test_10')
		parsed_data = validation(read_buffer)

		result(18, False, None, 'brackets/test_10')
	except Exception as e:
		result(18, True, e, 'brackets/test_10')



def test_not_valid_19():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}brackets/test_11')
		parsed_data = validation(read_buffer)

		result(19, False, None, 'brackets/test_11')
	except Exception as e:
		result(19, True, e, 'brackets/test_11')



def test_not_valid_20():
	try:
		read_buffer = read_file(f'{INVALID_TESTS}test_12')
		parsed_data = validation(read_buffer)

		result(20, False, None, 'test_12')
	except Exception as e:
		result(20, True, e, 'test_12')









def test_not_valid_11():
	try:
		result(11, False, None, '')
	except Exception as e:
		result(11, True, e, '')



def test_not_valid_12():
	try:
		result(12, False, None, '')
	except Exception as e:
		result(12, True, e, '')



def test_not_valid_13():
	try:
		result(13, False, None, '')
	except Exception as e:
		result(13, True, e, '')



def test_not_valid_14():
	try:
		result(14, False, None, '')
	except Exception as e:
		result(14, True, e, '')



def test_not_valid_15():
	try:
		result(15, False, e, '')
	except Exception as e:
		result(15, True, e, '')






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

	test_not_valid_1()
	test_not_valid_2()
	test_not_valid_3()
	test_not_valid_4()
	test_not_valid_5()
	test_not_valid_6()
	test_not_valid_7()
	test_not_valid_8()
	test_not_valid_9()
	test_not_valid_10()
	test_not_valid_11()
	test_not_valid_12()
	test_not_valid_13()
	test_not_valid_14()
	test_not_valid_15()
	test_not_valid_16()
	test_not_valid_17()
	test_not_valid_18()
	test_not_valid_19()
	# test_not_valid_20()
	# test_not_valid_21()
	# test_not_valid_22()
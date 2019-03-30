import pytest

from src.read_file import read_buffer
from src.new_validation import *
from src.new_solution import start_solution

FULL_PATH = '/Users/abaranov/projects/expert_system'

VALID_ALGORITHM_TEST = f'{FULL_PATH}/test/algorithm_tests/valid_test_'



def test_algorithm_00001():
    buff = read_buffer(f'{VALID_ALGORITHM_TEST}00001.txt')
    parsed_data = validation(buff)

    expected_result = {
        'A': 'True',
        'F': 'True',
        'K': 'True',
        'P': 'True',

    }
    facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in parsed_data['unknown_vars']}


def test_algorithm_00002():
    buff = read_buffer(f'{VALID_ALGORITHM_TEST}00002.txt')
    parsed_data = validation(buff)

    expected_result = {
        'A': 'False',

    }
    facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in parsed_data['unknown_vars']}


def test_algorithm_00003():
    buff = read_buffer(f'{VALID_ALGORITHM_TEST}00003.txt')
    parsed_data = validation(buff)

    expected_result = {
        'A': 'False',
    }
    facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in parsed_data['unknown_vars']}


def test_algorithm_00004():
    buff = read_buffer(f'{VALID_ALGORITHM_TEST}00004.txt')
    parsed_data = validation(buff)

    expected_result = {
        'A': 'True',
    }
    facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in parsed_data['unknown_vars']}


def test_algorithm_00005():
    buff = read_buffer(f'{VALID_ALGORITHM_TEST}00005.txt')
    parsed_data = validation(buff)

    expected_result = {
        'A': 'False',
    }
    facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in parsed_data['unknown_vars']}


def test_algorithm_00006():
    buff = read_buffer(f'{VALID_ALGORITHM_TEST}00006.txt')
    parsed_data = validation(buff)

    expected_result = {
        'E': 'False',
    }
    facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in parsed_data['unknown_vars']}


def test_algorithm_00007():
    buff = read_buffer(f'{VALID_ALGORITHM_TEST}00007.txt')
    parsed_data = validation(buff)

    expected_result = {
        'B': 'False',
        'D': 'True',
        'F': 'False',
    }
    facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in parsed_data['unknown_vars']}


def test_algorithm_00008():
    buff = read_buffer(f'{VALID_ALGORITHM_TEST}00008.txt')
    parsed_data = validation(buff)

    expected_result = {
        'C': 'True',
        'F': 'False',
        'I': 'False',
        'L': 'False',
    }
    facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in parsed_data['unknown_vars']}


def test_algorithm_00009():
    buff = read_buffer(f'{VALID_ALGORITHM_TEST}00009.txt')
    parsed_data = validation(buff)

    expected_result = {
        'C': 'True',
        'F': 'True',
        'I': 'True',
        'L': 'False',
    }
    facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in parsed_data['unknown_vars']}


def test_algorithm_00010():
    buff = read_buffer(f'{VALID_ALGORITHM_TEST}00010.txt')
    parsed_data = validation(buff)

    expected_result = {
        'C': 'False',
        'F': 'True',
        'I': 'True',
        'L': 'False',
    }
    facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in parsed_data['unknown_vars']}


def test_algorithm_00011():
    buff = read_buffer(f'{VALID_ALGORITHM_TEST}00011.txt')
    parsed_data = validation(buff)

    expected_result = {
        'D': 'True',
        'I': 'True',
    }
    facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in parsed_data['unknown_vars']}


def test_algorithm_00012():
    buff = read_buffer(f'{VALID_ALGORITHM_TEST}00012.txt')
    parsed_data = validation(buff)

    expected_result = {
        'C': 'True',
        'A': 'True',
    }
    facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in parsed_data['unknown_vars']}


def test_algorithm_00013():
    buff = read_buffer(f'{VALID_ALGORITHM_TEST}00013.txt')
    parsed_data = validation(buff)

    expected_result = {
        'D': 'True',
        'E': 'False',
        'C': 'True',
    }
    facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in parsed_data['unknown_vars']}


def test_algorithm_00014():
    buff = read_buffer(f'{VALID_ALGORITHM_TEST}00014.txt')
    parsed_data = validation(buff)

    expected_result = {
        'C': 'True',
        'D': 'True',
        'G': 'False',
        'H': 'False',
        'K': 'True',
        'L': 'False',
        'O': 'False',
        'P': 'True',
        'S': 'False',
        'T': 'False',
        'X': 'False',
        'Y': 'False',
        'Z': 'False'
    }
    facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in parsed_data['unknown_vars']}


def test_algorithm_00015():
    buff = read_buffer(f'{VALID_ALGORITHM_TEST}00015.txt')
    parsed_data = validation(buff)

    expected_result = {
        'C': 'True'
    }
    facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in parsed_data['unknown_vars']}


if __name__ == '__main__':
    pytest.main(['-vv'])
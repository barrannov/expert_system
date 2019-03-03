import pytest

from src.read_file import *
from src.validation import *
from src.new_solution import start_solution

VALID_ALGORITHM_TEST = 'test/algorithm_tests/valid_test_'


def test_algorithm_00001():
    read_buffer = read_file(f'{VALID_ALGORITHM_TEST}00001.txt')
    parsed_data = validation(read_buffer)

    expected_result = {
        'A': 'True',
        'F': 'True',
        'K': 'True',
        'P': 'True',

    }
    facts, unknown_facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in unknown_facts}


def test_algorithm_00002():
    read_buffer = read_file(f'{VALID_ALGORITHM_TEST}00002.txt')
    parsed_data = validation(read_buffer)

    expected_result = {
        'A': 'False',

    }
    facts, unknown_facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in unknown_facts}


def test_algorithm_00003():
    read_buffer = read_file(f'{VALID_ALGORITHM_TEST}00003.txt')
    parsed_data = validation(read_buffer)

    expected_result = {
        'A': 'False',
    }
    facts, unknown_facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in unknown_facts}


def test_algorithm_00004():
    read_buffer = read_file(f'{VALID_ALGORITHM_TEST}00004.txt')
    parsed_data = validation(read_buffer)

    expected_result = {
        'A': 'True',
    }
    facts, unknown_facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in unknown_facts}


def test_algorithm_00005():
    read_buffer = read_file(f'{VALID_ALGORITHM_TEST}00005.txt')
    parsed_data = validation(read_buffer)

    expected_result = {
        'A': 'True',
    }
    facts, unknown_facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in unknown_facts}


def test_algorithm_00006():
    read_buffer = read_file(f'{VALID_ALGORITHM_TEST}00006.txt')
    parsed_data = validation(read_buffer)

    expected_result = {
        'E': 'False',
    }
    facts, unknown_facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in unknown_facts}


def test_algorithm_00007():
    read_buffer = read_file(f'{VALID_ALGORITHM_TEST}00007.txt')
    parsed_data = validation(read_buffer)

    expected_result = {
        'B': 'False',
        'D': 'True',
        'F': 'False',
    }
    facts, unknown_facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in unknown_facts}


def test_algorithm_00008():
    read_buffer = read_file(f'{VALID_ALGORITHM_TEST}00008.txt')
    parsed_data = validation(read_buffer)

    expected_result = {
        'C': 'True',
        'F': 'False',
        'I': 'False',
        'J': 'False',
    }
    facts, unknown_facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in unknown_facts}


def test_algorithm_00009():
    read_buffer = read_file(f'{VALID_ALGORITHM_TEST}00009.txt')
    parsed_data = validation(read_buffer)

    expected_result = {
        'C': 'True',
        'F': 'True',
        'I': 'True',
        'L': 'False',
    }
    facts, unknown_facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in unknown_facts}


def test_algorithm_00010():
    read_buffer = read_file(f'{VALID_ALGORITHM_TEST}00010.txt')
    parsed_data = validation(read_buffer)

    expected_result = {
        'C': 'False',
        'F': 'True',
        'I': 'True',
        'L': 'False',
    }
    facts, unknown_facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in unknown_facts}


def test_algorithm_00011():
    read_buffer = read_file(f'{VALID_ALGORITHM_TEST}00011.txt')
    parsed_data = validation(read_buffer)

    expected_result = {
        'D': 'True',
        'I': 'True',
    }
    facts, unknown_facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in unknown_facts}


def test_algorithm_00012():
    read_buffer = read_file(f'{VALID_ALGORITHM_TEST}00012.txt')
    parsed_data = validation(read_buffer)

    expected_result = {
        'C': 'True',
        'A': 'True',
    }
    facts, unknown_facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in unknown_facts}


def test_algorithm_00013():
    read_buffer = read_file(f'{VALID_ALGORITHM_TEST}00013.txt')
    parsed_data = validation(read_buffer)

    expected_result = {
        'D': 'True',
        'E': 'False',
        'C': 'True',
    }
    facts, unknown_facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in unknown_facts}


def test_algorithm_00014():
    read_buffer = read_file(f'{VALID_ALGORITHM_TEST}00014.txt')
    parsed_data = validation(read_buffer)

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
    facts, unknown_facts = start_solution(parsed_data)
    assert expected_result == {fact: facts.get(fact) for fact in unknown_facts}


if __name__ == '__main__':
    pytest.main(['-vv'])
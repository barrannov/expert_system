from typing import Dict, Tuple, List
from src.parser import solve_condition


rules = list()

facts = dict()

# list of initially unknown facts
unknown_facts = list()

# determined facts are appended to this list
determined_facts = list()

# facts which are impossible to terminate
undetermined_facts = list()

separator = "=>"


def _initialize(initial_values):
    global rules
    global facts

    rules = initial_values['conditions']
    for name, value in initial_values['vars'].items():
        if value is None:
            unknown_facts.append(name)
            facts[name] = 'False'
        else:
            facts[name] = value
            if value is True:
                determined_facts.append(name)


def start_solution(initial_values: dict):

    _initialize(initial_values)
    # TODO go in a correct order

    for u_fact in unknown_facts:
        if facts[u_fact] not in determined_facts:
            fact_value = _find_with_recursion(u_fact)
            if fact_value is None:
                undetermined_facts.append(
                    u_fact
                )
            else:
                determined_facts.append(u_fact)
                facts[u_fact] = fact_value

    return facts, unknown_facts


def _get_new_rule(unknown_fact: str, checked_rules: list) -> tuple:
    # TODO return rule for finding value of fact
    #   if there are no rules with unknown_fact in second part of rule
    #   try to find with rule with fact in first part, else return empty tuple

    for rule in rules:
        if unknown_fact in rule and rule not in checked_rules:
            first_part = rule[:rule.index(separator)]
            if unknown_fact in first_part:
                continue
            else:
                return rule


def _get_unknown_fact_from_rule(current_rule, current_unkown_fact) -> str:
    # TODO find unknow fact which doesn't allow us to find value of
    #   current_unknow fact

    split_index = current_rule.index('=>')
    first_part = current_rule[:split_index]
    second_part = current_rule[split_index + 1:]

    for fact in current_rule:
        if (fact not in determined_facts) \
                and (fact is not current_unkown_fact) \
                and (fact not in undetermined_facts) \
                and (fact in facts):
            return fact


def _convert_rule_into_condition(rule, unkown_fact=None, possible_value=None):
    final_condition = []

    for token in rule:
        if unkown_fact and possible_value:
            if token == unkown_fact:
                final_condition.append(possible_value)
            else:
                final_condition.append(facts.get(token))
        else:
            final_condition.append(facts.get(token))

    return final_condition


def _only_add_in_rule(rule):
    for token in rule:
        if token in facts or token == '+' or token == '!' and token in determined_facts:
            continue
        else:
            return False
    return True


def _count_unknown_fact(rule, unknown_fact):
    split_index = rule.index('=>')
    first_part = rule[:split_index]
    second_part = rule[split_index + 1:]

    if unknown_fact in first_part:
        first_part, second_part = second_part, first_part

    first_condition = _convert_rule_into_condition(first_part)
    first_value = solve_condition(first_condition)

    for b in ('False', 'True'):
        second_condition = _convert_rule_into_condition(second_part, unknown_fact, b)
        second_value = solve_condition(second_condition)

        if second_value == first_value:
            if _only_add_in_rule(second_part) and first_value == 'True':
                for token in second_part:
                    if token in facts and token is not unknown_fact:
                        determined_facts.append(token)
                        facts[token] = 'True'
            return b


def _find_with_recursion(unknown_fact, checked_rules=None):
    if checked_rules is None:
        checked_rules = []

    rule = _get_new_rule(unknown_fact, checked_rules)
    if not rule:
        return 'False'

    checked_rules.append(rule)

    unknown_value_exists = True
    while unknown_value_exists:
        unknown_fact_in_rule = _get_unknown_fact_from_rule(rule, unknown_fact)
        if unknown_fact_in_rule is not None:
            # TODO save found value directly into dict and everywhere
            found_value = _find_with_recursion(unknown_fact_in_rule, checked_rules)
            if found_value is None:
                undetermined_facts.append(
                    unknown_fact_in_rule
                )
            else:
                determined_facts.append(unknown_fact_in_rule)
                facts[unknown_fact_in_rule] = found_value
        else:
            unknown_value_exists = False

    return _count_unknown_fact(rule, unknown_fact)

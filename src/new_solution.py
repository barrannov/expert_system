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


    #TODO initialize rules, facts, unknown_facts
    pass


def start_solution(initial_values:dict):

    _initialize(initial_values)
    for u_fact in unknown_facts:
        fact_value = _find_with_recursion(u_fact)
        if fact_value is None:
            undetermined_facts.append(
                u_fact
            )
        else:
            determined_facts.append(u_fact)
            facts[u_fact] = fact_value

    return facts, unknown_facts


def _get_new_rule(unknown_fact:str, checked_rules:list) -> tuple:
    # TODO return rule for finding value of fact
    #   if there are no rules with unknown_fact in second part of rule
    #   try to find with rule with fact in first part, else return empty tuple


    possible_rule = ()
    for rule in rules:
        if unknown_fact in rule and rule not in checked_rules:
            first_part = rule[:rule.index(separator)]
            if unknown_fact in first_part:
                possible_rule = rule
            else:
                return rule
    return possible_rule


def _get_unknown_fact_from_rule(current_rule, current_unkown_fact) -> str:
    # TODO find unknow fact which doesn't allow us to find value of
    #   current_unknow fact
    rule_undetermined_facts = []

    for fact in current_rule:
        if (
                fact not in determined_facts) and (
                fact is not current_unkown_fact):
            rule_undetermined_facts.append(fact)

    return rule_undetermined_facts


def _count_unknown_fact(rule, unknown_fact):
    final_condition = []
    for b in ('True', 'False'):
        for token in rule:
            if token == unknown_fact:
                token = b
            final_condition.append(
                facts.get(token)
            ) if token in facts else final_condition.append(token)
        res_value = solve_condition(final_condition)
        if res_value == 'True':
            return b


def _find_with_recursion(unknown_fact, checked_rules=None):
    if checked_rules is None:
        checked_rules = []

    rule = _get_new_rule(unknown_fact, checked_rules)
    checked_rules.append(rule)
    if rule == ():
        return None

    unknown_fact_in_rule = _get_unknown_fact_from_rule(rule, unknown_fact)
    if unknown_fact_in_rule is not []:
        # TODO save found value directly into dict and everywhere
        for new
        _find_with_recursion(unknown_fact_in_rule, checked_rules)

    return _count_unknown_fact(rule, unknown_fact)

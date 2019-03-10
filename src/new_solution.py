from src.parser import solve_expression

rules = tuple()

facts = dict()

# list of initially unknown facts
unknown_facts = tuple()

# determined facts are appended to this list
determined_facts = list()

# facts which are impossible to terminate
undetermined_facts = list()

# visited rules for facts
visited_rules = dict()

separator = "=>"

TRUE = 'True'
FALSE = 'False'

OPERATORS = ('+', '!', '^', '(', ')', '|', '=>', '<=>')


def _save_rule(rule, value):
    if facts.get(rule) != 'True':
        facts[rule] = value
        if rule not in determined_facts:
            determined_facts.append(rule)


def _initialize(initial_values):
    global rules
    global facts
    global unknown_facts
    global determined_facts
    global undetermined_facts
    global visited_rules

    visited_rules = dict()
    unknown_facts = list()
    determined_facts = list()
    undetermined_facts = list()
    rules = list()
    facts = dict()

    rules = initial_values['conditions']
    for name, value in initial_values['vars'].items():
        if value is None:
            unknown_facts.append(name)
            facts[name] = FALSE
        else:
            facts[name] = value
            if value == 'True':
                determined_facts.append(name)

    for rule_i, rule in enumerate(rules):
        try:
            split_index = rule.index('=>')
        except ValueError:
            split_index = rule.index('<=>')

        conclusion = rule[split_index + 1:]

        for token in conclusion:
            if not token in OPERATORS:
                if token not in visited_rules:
                    visited_rules[token] = []
                visited_rules[token].append(rule_i)
                # rule index; visited or not


def start_solution(initial_values: dict):
    _initialize(initial_values)

    for u_fact in unknown_facts:
        for rule_i, rule in enumerate(visited_rules[u_fact]):
            if facts.get(u_fact) != 'True':
                fact_value = _find_with_recursion(u_fact, rule=rules[rule])
                _save_rule(u_fact, fact_value)
        #
        # if facts[u_fact] not in determined_facts:
        #     fact_value = _find_with_recursion(u_fact)
        #     if fact_value is None:
        #         undetermined_facts.append(
        #             u_fact
        #         )
        #     else:
        #         determined_facts.append(u_fact)
        #         facts[u_fact] = fact_value
    return facts


def _get_new_rule(unknown_fact: str, checked_rules: list) -> tuple:

    for rule_i, rule in enumerate(rules):
        if unknown_fact in rule and rule not in checked_rules:
            first_part = rule[:rule.index(separator)]
            if unknown_fact in first_part:
                continue
            else:
                return rule


def _get_unknown_fact_from_rule(current_rule, current_unkown_fact):

    split_index = current_rule.index('=>')
    condition = current_rule[:split_index]
    conclusion = current_rule[split_index + 1:]

    # check possible solution
    if current_unkown_fact not in condition:
        condition_exp = _convert_rule_into_expression(condition)
        condition_res = solve_expression(condition_exp, condition=True)
        if condition_res:
            for b in ('True', 'False'):
                conclusion_exp = _convert_rule_into_expression(
                    conclusion, unkown_fact=current_unkown_fact, possible_value=b)
                conclusion_res = solve_expression(conclusion_exp, conclusion=True)
                if conclusion_res in ('True', 'False'):
                    return None

    for fact in condition:
        if (fact not in determined_facts) \
                and (fact is not current_unkown_fact) \
                and (fact not in undetermined_facts) \
                and (fact in facts):
            return fact

    for fact in conclusion:
        if (fact not in determined_facts) \
                and (fact is not current_unkown_fact) \
                and (fact not in undetermined_facts) \
                and (fact in facts):
            return fact


def _convert_rule_into_expression(rule, unkown_fact=None, possible_value=None):
    final_condition = []

    for token in rule:
        if unkown_fact and token == unkown_fact:
            final_condition.append(possible_value)
        elif token in determined_facts:
            final_condition.append(facts.get(token))
        elif token in OPERATORS:
            final_condition.append(token)
        elif token == TRUE or token == FALSE:
            final_condition.append(token)
        else:
            final_condition.append(None)

    return final_condition


def _only_add_in_rule(rule):
    for token in rule:
        if token in facts or token == '+' or token == '!' and token in determined_facts:
            continue
        else:
            return False
    return True


def _count_unknown_fact(rule, unknown_fact):
    if not rule:
        return FALSE

    split_index = rule.index('=>')
    condition = rule[:split_index]
    conclusion = rule[split_index + 1:]

    first_condition = _convert_rule_into_expression(condition)
    first_value = solve_expression(first_condition, condition=True)

    for b in (FALSE, TRUE):
        second_condition = _convert_rule_into_expression(conclusion, unknown_fact, b)
        second_value = solve_expression(second_condition, conclusion=True)

        if second_value == first_value:
            if _only_add_in_rule(conclusion) and first_value == TRUE:
                for token in conclusion:
                    if token in facts and token is not unknown_fact:
                        _save_rule(token, TRUE)
            return b
    return FALSE


def _find_with_recursion(unknown_fact, rule=None, checked_rules=None):
    if checked_rules is None:
        checked_rules = []

    if not rule:
        rule = _get_new_rule(unknown_fact, checked_rules)

    if rule:
        checked_rules.append(rule)

        unknown_value_exists = True
        while unknown_value_exists:
            unknown_fact_in_rule = _get_unknown_fact_from_rule(rule, unknown_fact)
            if unknown_fact_in_rule is not None:
                found_value = _find_with_recursion(unknown_fact_in_rule, checked_rules=checked_rules)
                if found_value is None:
                    undetermined_facts.append(unknown_fact_in_rule)
                else:
                    _save_rule(unknown_fact_in_rule, found_value)
            else:
                unknown_value_exists = False

    return _count_unknown_fact(rule, unknown_fact)

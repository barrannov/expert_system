from src.parser import solve_condition
import re

all_data = {}


def _prepare_conditions(conditions):
    new_conditions = []

    for condition in conditions:
        # we suppose that there is always '=>' or '<=>' present
        sep = '=>' if '=>' in condition else '<=>'
        sep_index = condition.index(sep)

        for i, token in enumerate(condition):
            if re.match('^!?[A-Z]$',token):
                condition[i] = {
                    'var': token.replace('!', ''),
                    'neg': '!' in token
                }

        new_conditions.append({
            'left_part': condition[:sep_index],
            'sep': sep,
            'right_part': condition[sep_index + 1:]
        })
    return new_conditions


def _get_condition_with_unknown(unknown, exept_conds=None):
    global all_data

    exept_conds = [] if exept_conds is None else exept_conds
    conditions = all_data['conditions']

    all_conds_with_unknown = []
    for cond in conditions:
        variables = [token for token in cond['right_part'] if token not in all_data['operators']]
        if (any(
                token['var'] == unknown['var'] for token in variables)
                and cond not in exept_conds):
            all_conds_with_unknown.append(cond)

    shortest = all_conds_with_unknown[0]
    for cond in all_conds_with_unknown:
        if len(cond['right_part']) < len(shortest):
            shortest = cond

    return shortest


def _get_unknown():
    global all_data
    for var_name, value in all_data['vars'].items():
        if value is None:
            return var_name
    return None


def _get_first_unknown_cond():
    for cond in all_data['conditions']:
        unknown = _unknown_exists(cond['right_part'])
        if unknown:
            return unknown


def solve(data):
    global all_data

    data['conditions'] = _prepare_conditions(data['conditions'])
    data['operators'] = ["^", "!", "+", "|", "<=>", "=>", "(", ")"]
    data['visited_conds'] = {}
    for var in data['vars']:
        # create initial list of checked conditions for each variable
        data['visited_conds'][var] = []
    all_data = data
    unknown = _get_first_unknown_cond()
    recursion_solve(unknown)


def _unknown_exists(cond_part, except_fact=None):
    global all_data
    for token in cond_part:
        if token in all_data['operators']:
            continue
        var_name = token['var']
        if (var_name in all_data['vars'] and all_data['vars'][var_name] is None
                and var_name != except_fact):
            return token


def _solve_left_part(left_part):
    res = solve_condition(left_part, all_data['vars'])
    return {'var':res, 'neg':False}


def _resolve_right_part(unknown, res_left_part, sep, right_part):

    right_true = list(right_part)
    right_false = list(right_part)
    for i, token in enumerate(right_true):
        if token in all_data['operators']:
            continue
        if token['var'] == unknown['var']:
            right_true[i] = {'var': 'True', 'neg': token['neg']}
            right_false[i] = {'var': 'False', 'neg': token['neg']}

    true_option = [res_left_part] + [sep] + right_true
    false_option = [res_left_part] + [sep] + right_false
    true_option_solve = solve_condition(true_option, all_data['vars'])
    false_option_solve = solve_condition(false_option, all_data['vars'])
    if true_option_solve == false_option_solve:
        return None
    return true_option_solve if true_option_solve else false_option_solve


def _all_vars_known():
    return all(var is not None for var in all_data['vars'])


def _all_conditions_were_visited():
    conds_amount = len(all_data['conditions'])
    return all(
        len(all_data['visited_conds'][var]) == conds_amount
        for var in all_data['vars']
    )


def _set_obvious_right_part(res_left_part,sep , right_part):
    variables = [
        token for token in right_part if isinstance(token, dict) and token['var'] in all_data['vars']
    ]
    operators = [
        token for token in right_part if token in all_data['operators']
    ]
    if all(o == '+' for o in operators):
        right_true = {'var': 'True', 'neg': False}
        right_false = {'var': 'False', 'neg': False}

        true_option = [res_left_part] + [sep] + [right_true, ]
        false_option = [res_left_part] + [sep] + [right_false]
        true_option_solve = solve_condition(true_option, all_data['vars'])
        false_option_solve = solve_condition(false_option, all_data['vars'])
        if true_option_solve == false_option_solve:
            return right_part

        for v in variables:
            all_data['vars'][v['var']] = True if true_option_solve else False

    return right_part


def recursion_solve(unknown):
    condition = _get_condition_with_unknown(
        unknown, exept_conds=all_data['visited_conds'][unknown['var']]
    )
    left_part = list(condition['left_part'])
    right_part = list(condition['right_part'])
    left_unknown = _unknown_exists(left_part)
    if left_unknown:
        all_data['visited_conds'][unknown['var']].append(condition)
        recursion_solve(left_unknown)
    res_left_part = _solve_left_part(left_part)

    right_part = _set_obvious_right_part(res_left_part, condition['sep'], right_part)
    right_unknown = _unknown_exists(right_part, except_fact=unknown['var'])
    if right_unknown:
        all_data['visited_conds'][unknown['var']].append(condition)
        recursion_solve(right_unknown)
    else:
        value = _resolve_right_part(
            unknown, res_left_part, condition['sep'], right_part
        )
        if value is None:
            # both True and False values are possible
            pass
        all_data['vars'][unknown['var']] = value
        if _all_vars_known() or _all_conditions_were_visited():
            return all_data
    recursion_solve(_get_unknown())

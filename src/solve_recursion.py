from src.parser import solve_condition

all_data = {}


def _prepare_conditions(conditions):
    new_conditions = []

    for condition in conditions:
        # we suppose that there is always '=>' or '<=>' present
        sep = '=>' if '=>' in condition else '<=>'
        sep_index = condition.index(sep)

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
    for cond in conditions:
        if (any(token == unknown for token in cond['right_part'])
                and cond not in exept_conds):
            return cond


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
        if (token in all_data['vars'] and all_data['vars'][token] is None
                and token != except_fact):
            return token


def _solve_left_part(left_part):
    res = solve_condition(left_part, all_data['vars'])
    return res


def _resolve_right_part(unknown, res_left_part, sep, right_part):
    un_index = right_part.index(unknown)
    right_true = list(right_part)
    right_false = list(right_part)

    right_true[un_index] = 'True'
    right_false[un_index] = 'False'
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
    variables = [token for token in right_part if token in all_data['vars']]
    operators = [token for token in right_part if token not in variables]
    if all(o == '+' for o in operators):
        right_true = 'True'
        right_false  = 'False'

        true_option = [res_left_part] + [sep] + [right_true]
        false_option = [res_left_part] + [sep] + [right_false]
        true_option_solve = solve_condition(true_option, all_data['vars'])
        false_option_solve = solve_condition(false_option,
                                         all_data['vars'])
        if true_option_solve == false_option_solve:
            return None

        for v in variables:
            all_data['vars'][v] = true_option_solve if \
                true_option_solve else false_option_solve

    return right_part

def recursion_solve(unknown):
    condition = _get_condition_with_unknown(
        unknown, exept_conds=all_data['visited_conds'][unknown]
    )
    left_part = condition['left_part']
    right_part = condition['right_part']
    left_unknown = _unknown_exists(left_part)
    if left_unknown:
        all_data['visited_conds'][unknown].append(condition)
        recursion_solve(left_unknown)
    res_left_part = _solve_left_part(left_part)

    right_part = _set_obvious_right_part(res_left_part, condition['sep'], right_part)
    right_unknown = _unknown_exists(right_part, except_fact=unknown)
    if right_unknown:
        all_data['visited_conds'][unknown].append(condition)
        recursion_solve(right_unknown)
    else:
        value = _resolve_right_part(
            unknown, res_left_part, condition['sep'], right_part
        )
        if value is None:
            # both True and False values are possible
            pass
        all_data['vars'][unknown] = value
        if _all_vars_known() or _all_conditions_were_visited():
            return all_data
    recursion_solve(_get_unknown())

from src.algorithms import solve_condition

def _prepare_conditions(conditions):
    new_conditions = []

    for condition in conditions:
        # we suppose that there is always '=>' or '<=>' present
        sep = '=>' if '=>' in condition else '<=>'
        sep_index = condition.index(sep)

        new_conditions.append({
            'first_part': condition[:sep_index],
            'sep': sep,
            'second_part': condition[sep_index:]
        })
    return new_conditions


def solve(data):
    data['conditions'] = _prepare_conditions(data['conditons'])
    start_solving(data)


def start_solving(data, vertical_graph=None, var_index=0):
    all_vars = data['vars']
    all_unknown_vars = [v for v in data['vars'] if v is None]
    all_known_vars = [v for v in data['vars'] if v is not None]
    if vertical_graph is None:
        vertical_graph = dict()
    for cond in data['conditions']:
        if (all_unknown_vars[var_index] in cond['second_part'] or
            f'!{all_unknown_vars[var_index]}' in cond['second_part']) and \
                cond not in vertical_graph[all_unknown_vars[var_index]]:
            res = solve_condition(cond['first_part'])
            if res is True:
                pass
            elif res is False:
                pass
            else:
                # we get name of variable in res which is not found yet but
                # occurred in condition,  we need to call recursion to find
                # value of that variable
                start_solving(
                    data,
                    vertical_graph=vertical_graph,
                    var_index=all_unknown_vars.index(res)
                )
from src.parser import solve_condition

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
    data['conditions'] = _prepare_conditions(data['conditions'])
    start_solving(data)

all_data = []
def start_solving(data, vertical_graph=None, var_index=0):
    global all_data

    all_data = data
    # all_unknown_vars = [v for v in data['vars'] if data['vars'][v] is None]
    # all_known_vars = [v for v in data['vars'] if v is not None]
    # if vertical_graph is None:
    #     vertical_graph = []
    # for cond in data['conditions']:
    #     if (data['vars'][var_index] in cond['second_part'] or
    #         f"!{data['vars'][var_index]}" in cond['second_part']) and \
    #             cond not in vertical_graph[data['vars'][var_index]]:
    #         vertical_graph
    #         res = solve_condition(cond['first_part'], data)
    #         if res is True or res is False:
    #             new_cond = [res]+cond[1]+cond[2]
    #             data['vars'][var_index] = solve_condition(new_cond, data)
    #         else:
    #             # we get name of variable in res which is not found yet but
    #             # occurred in condition,  we need to call recursion to find
    #             # value of that variable
    #             start_solving(
    #                 data,
    #                 vertical_graph=vertical_graph,
    #                 var_index=data['vars'].index(res)
    #             )


a = 5
def recurssion_solve(unknown):
    global all_data

    condition = get_condition_with_unknown(unknown)
    left_part = condition['left_part']
    right_part = condition['right_part']
    if unknown_exists(left_part):
        left_unknown = get_unknown_from_condition(condition)
        recurssion_solve(left_unknown)
    res_left_part = solve_left_part(left_part)
    if not unknown_exists(right_part, excpet=unknown):
        value = resolve_right_part(res_left_part, right_part)
        write_to_data(var_name=unknown, value=value)
        if all_known():
            return
    right_unknown = get_unknown_from_condition(condition, exept=unknown)
    recurssion_solve(right_unknown)

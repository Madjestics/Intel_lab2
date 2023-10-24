import functions
import json


def read_json(filename):
    with open(filename, 'r', encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def parse(param):
    l = []
    if isinstance(param[0], list):
       for item in param:
           parse(item)
    else:
        func = functions.all_functions[param[0]]
        for i in range(1, len(param)):
            if (not isinstance(param[i], list)):
                args = param[1:]
                if len(args)>1 and args[1] in functions.all_functions:
                    return func(args[0], functions.all_functions[args[1]]())
                else:
                    l = args
            else:
                l.append(parse(param[i]))
        return func(*l)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = read_json('lab2.json')
    for item in data['rules']:
        if_part = item['if']
        action_part = item['action']
        condition = parse(if_part)
        if condition:
            parse(action_part)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

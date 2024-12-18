name_list = {
    'Alex': '1',
    'Vova': '2',
    'Vasya': '3',
    'John': '4',
    'Igor': '5',
    'Nikita': '6',
}
new_list = {}
for name, value in name_list.items():
    new_list[f"{name}_{value}"] = value

new_list = {f"{name}_{value}": value
            for name, value in name_list.items()}

new_list = dict(map(lambda el: (f"{el[0]}_{el[1]}", el[1]), name_list.items()))

print(new_list)

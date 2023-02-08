# only with python 3.10+
# manage virtual envs with conda:
# https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#viewing-a-list-of-your-environments

cities_dicts = [
    {'name': 'Pau', 'cp': '64000', 'pop': 77000},
    {'name': 'Toulouse', 'cp': '31000', 'pop': 470000},
    {'name': 'Bordeaux', 'cp': '33000', 'pop': 250000},
    {'name': 'Bayonne', 'cp': '64100', 'pop': 49000},
    {'name': 'Lée', 'cp': '64320', 'pop': 1200},
]

match cities_dicts:
    case [first_city, *others]:
        print("First city:", first_city)
        print("Others:", others)
import departement.city as cy

cities_tuples = [
    ('Pau', '64000', 77000),
    ('Toulouse', '31000', 470000),
    ('Bordeaux', '33000', 250000),
    ('Bayonne', '64100', 49000),
    ('Lée', '64320', 1200),
]

cities_dicts = cy.convertCitiesTuplesToDicts(cities_tuples)
print(cities_dicts)
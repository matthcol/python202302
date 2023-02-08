print("Import module departement.city")

def convertCitiesTuplesToDicts(cities_tuples):
    """convert list of cities as tuples (name, code postal, population)
    to list of cities as dicts with keys name, cp and pop
    """
    return [ 
        {
            "name": name,
            "cp": cp,
            "pop": pop
        } for name, cp, pop  in cities_tuples 
    ]
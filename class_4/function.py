def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

# Docstring
def population_density(population, land_area):
    """Calculate the population density of an area.

    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.

    OUTPUT: 
    population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area

    # Função Lambida
    def multiply(x, y):
        return x * y
    
    multiply = lambda x, y: x * y

    
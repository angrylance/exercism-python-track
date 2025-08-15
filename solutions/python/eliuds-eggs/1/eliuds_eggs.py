# Solution to https://exercism.org/tracks/python/exercises/eliuds-eggs

# Solution 1 using bin()
# def egg_count(display_value):
#     return sum(int(x) for x in bin(display_value)[2:])


# Solution 2 sum + f"{var:b}""
def egg_count(display_value):
    return sum(int(x) for x in f"{display_value:b}")

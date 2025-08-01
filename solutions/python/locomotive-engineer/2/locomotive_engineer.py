"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    # Solution 1:
    # first, second, *rest = each_wagons_id
    # reordered = [*rest, first, second]
    # (*wagons,) = [reordered[0], *missing_wagons, *reordered]
    # return wagons

    # Solution 2 (better unpacking-packing)
    first, second, loco, *rest = each_wagons_id
    return [loco, *missing_wagons, *rest, first, second]


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    updated_route = {**route, "stops": list(kwargs.values())}
    return updated_route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    # Solution 1 with for loop:
    # correct_order = []
    # for col in range(len(wagons_rows)):
    #     new_train = []
    #     for row in wagons_rows:
    #         new_train.append(row[col])
    #     correct_order.append(new_train)
    # return correct_order

    # Solution 2 using zip and list comprehension:
    return [list(row) for row in zip(*wagons_rows)]

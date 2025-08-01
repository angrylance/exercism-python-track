"""Functions to keep track and alter inventory."""

# # Solution 1 for create_inventory using Counter class
# from collections import Counter

# def create_inventory(items):
#     """Create a dict that tracks the amount (count) of each element on the `items` list.

#     :param items: list - list of items to create an inventory from.
#     :return: dict - the inventory dictionary.
#     """
#     inventory = Counter(items)
#     return dict(inventory)

##   Solution 2 - set and items.count - worse performance-wise that solution 1 and 3.
# def create_inventory(items):
#     """Create a dict that tracks the amount (count) of each element on the `items` list.

#     :param items: list - list of items to create an inventory from.
#     :return: dict - the inventory dictionary.
#     """
#     inventory = {}
#     for key in set(items):
#         inventory[key] = items.count(key)
#     return inventory


## Solution 3 - counting using .get() method:
def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {}
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


## Solution 1 - using Counter
# from collections import Counter


# def add_items(inventory, items):
#     """Add or increment items in inventory using elements from the items `list`.

#     :param inventory: dict - dictionary of existing inventory.
#     :param items: list - list of items to update the inventory with.
#     :return: dict - the inventory updated with the new items.
#     """
#     existing_inv = Counter(inventory)
#     new_inv = Counter(items)
#     existing_inv.update(new_inv)
#     return dict(existing_inv)


# Solution 2 - implementing counter using .get() method
def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items:
        if item in inventory:
            inventory[item] = max(0, inventory[item] - 1)
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    return [(item, count) for item, count in inventory.items() if count > 0]

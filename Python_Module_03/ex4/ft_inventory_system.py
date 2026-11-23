# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_inventory_system.py                             :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/15 14:32:35 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/15 14:32:37 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import sys


def main() -> None:
    inventory = {}
    total_args = len(sys.argv)
    if (total_args < 2):
        return
    i = 1
    print("=== Inventory System Analysis ===")
    while i < total_args:
        try:
            list_argv = sys.argv[i].split(":")
            if (len(list_argv) != 2):
                print(f"Error - invalid parameter {sys.argv[i]}")
                i += 1
                continue
            if list_argv[0] not in inventory:
                inventory[list_argv[0]] = int(list_argv[1])
            else:
                print(f"Redundant item '{list_argv[0]}' - discarding")
        except ValueError as e:
            print(f"Quantity error for '{list_argv[0]}': {e}")
        except Exception as e:
            print(f"{e}")
        i += 1
    print(f"Got inventory: {inventory}")
    items_list = []
    for key in inventory.keys():
        items_list.append(key)
    print(f"Item list: {items_list}")
    sum_items = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {sum_items}")
    key_item_most_abundant = list(inventory.keys())[0]
    value_item_most_abundant = list(inventory.values())[0]
    key_item_least_abundant = list(inventory.keys())[0]
    value_item_least_abundant = list(inventory.values())[0]
    for key, value in inventory.items():
        print(f"Item {key}: represents {(value/sum_items)*100:.1f}%")
        if value > value_item_most_abundant:
            value_item_most_abundant = value
            key_item_most_abundant = key
        if value < value_item_least_abundant:
            value_item_least_abundant = value
            key_item_least_abundant = key
    print(f"Item most abundant: {key_item_most_abundant}"
          f" with quantity {value_item_most_abundant}")
    print(f"Item least abundant: {key_item_least_abundant}"
          f" with quantity {value_item_least_abundant}")
    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()

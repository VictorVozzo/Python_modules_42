# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   scope_mysteries.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/07/07 19:04:57 by vivozzo-           #+#    #+#             #
#   Updated: 2026/07/10 11:41:17 by vivozzo-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    increase = 0

    def increase_counter() -> int:
        nonlocal increase
        increase += 1
        return increase

    return increase_counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def increase_power(power: int) -> int:
        nonlocal total_power
        total_power += power
        return total_power

    return increase_power


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchantment_item(item: str) -> str:
        return f"{enchantment_type} {item}"

    return enchantment_item


def memory_vault() -> dict[str, Callable]:
    storage = {}

    def store(item: tuple) -> None:
        storage[item[0]] = item[1]

    def recall(item: tuple) -> Any:
        if item[0] not in storage:
            return "Memory not found"
        else:
            return storage[item[0]]

    return {"store": store, "recall": recall}


if __name__ == "__main__":

    try:
        print("Testing mage counter:")
        counter_a = mage_counter()
        counter_b = mage_counter()
        print("counter_a call 1: ", counter_a())
        print("counter_a call 2: ", counter_a())
        print("counter_b call 1: ", counter_b())

        print("\nTesting spell accumulator: ")
        base = 100
        first_add = 20
        second_add = 30
        accumulator = spell_accumulator(base)
        print(f"Base {base}, add {first_add}: {accumulator(first_add)}")
        print(f"Base {base}, add {second_add}: {accumulator(second_add)}")

        print("\nTesting enchantment factory: ")
        factory_a = enchantment_factory("Flaming")
        factory_b = enchantment_factory("Frozen")
        print(factory_a("Sword"))
        print(factory_b("Shield"))

        print("\nTesting memory vault: ")
        first_item = ("secret", 42)
        second_item = ("unknown", 9000)
        print(f"first item: {first_item}")
        print(f"second item: {second_item}")
        warehouse = memory_vault()
        warehouse_store = warehouse["store"]
        warehouse_recall = warehouse["recall"]
        print(f"Store '{first_item[0]}' = {first_item[1]}")
        warehouse_store(first_item)
        print(f"Recall '{first_item[0]}': {warehouse_recall(first_item)}")
        print(f"Recall '{second_item[0]}': {warehouse_recall(second_item)}")
    except Exception as e:
        print(e)

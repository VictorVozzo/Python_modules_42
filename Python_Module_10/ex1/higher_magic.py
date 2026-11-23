# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   higher_magic.py                                     :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/07/07 16:33:53 by vivozzo-           #+#    #+#             #
#   Updated: 2026/07/10 11:38:34 by vivozzo-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from collections.abc import Callable


def storm(target: str, power: int) -> str:
    return f"Storm deals {power} damage to {target}"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combiner


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return conditional


def condition(target: str, power: int) -> bool:
    if power > 7:
        return True
    return False


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        spells_list = []
        for spell in spells:
            spells_list.append(spell(target, power))
        return spells_list
    return sequence


if __name__ == "__main__":
    test_values = [6, 11, 23, 35]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    try:
        print("Testing spell combiner(fireball and heal with "
              f"{test_targets[0]} and value = {test_values[0]}):\n")
        combined = spell_combiner(fireball, heal)
        result_combined = combined(test_targets[0], test_values[0])
        print(f"{result_combined[0]}, {result_combined[1]}")

        print("\nTesting power amplifier:\n")
        mega_fireball = power_amplifier(fireball, 3)
        print(f"Original: {fireball(test_targets[1], test_values[1])}")
        print(f"Amplified: {mega_fireball(test_targets[1], test_values[1])}")

        print("\nTesting conditional caster(value > 7) and heal function: \n")
        conditional = conditional_caster(condition, heal)
        print(f"{test_targets[2]} with {test_values[2]}: ",
              conditional(test_targets[2], test_values[2]))
        print(f"{test_targets[0]} with {test_values[0]}: ",
              conditional(test_targets[0], test_values[0]))

        print("\nTesting spell sequence with "
              f"{test_targets[3]} and value = {test_values[3]}: \n")
        sequence = spell_sequence([heal, fireball, storm])
        list_spells = sequence(test_targets[3], test_values[3])
        for spell in list_spells:
            print(spell)
    except Exception as e:
        print(e)

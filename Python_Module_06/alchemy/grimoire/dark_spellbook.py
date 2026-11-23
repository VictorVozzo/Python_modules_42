# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   dark_spellbook.py                                  :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/24 17:23:03 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/24 17:23:03 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    allowed_ingredients: list[str] = ["bats", "frogs", "arsenic", "eyeball"]
    return allowed_ingredients


def dark_spell_record(spell_name: str, ingredients: str) -> str:

    validate: str = dark_validate_ingredients(ingredients)
    if validate == f"({ingredients} - VALID)":
        return (f"Spell recorded: {spell_name} " + validate)
    else:
        return (f"Spell rejected: {spell_name} " + validate)

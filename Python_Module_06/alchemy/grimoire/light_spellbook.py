# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   light_spellbook.py                                 :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/24 15:55:18 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/24 15:55:18 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

def light_spell_allowed_ingredients() -> list[str]:
    allowed_ingredients: list[str] = ["earth", "air", "fire", "water"]
    return allowed_ingredients


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients

    validate: str = validate_ingredients(ingredients)
    if validate == f"({ingredients} - VALID)":
        return (f"Spell recorded: {spell_name} " + validate)
    else:
        return (f"Spell rejected: {spell_name} " + validate)

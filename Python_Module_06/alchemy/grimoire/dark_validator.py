# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   dark_validator.py                                  :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/24 17:23:31 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/24 17:23:31 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed_ingredients: list[str] = dark_spell_allowed_ingredients()
    if any(x in ingredients.lower() for x in allowed_ingredients):
        return (f"({ingredients} - VALID)")
    else:
        return (f"({ingredients} - INVALID)")

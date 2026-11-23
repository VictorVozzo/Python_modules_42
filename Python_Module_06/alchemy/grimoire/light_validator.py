# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   light_validator.py                                 :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/24 16:07:43 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/24 16:07:43 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients: list[str] = light_spell_allowed_ingredients()
    if any(x in ingredients.lower() for x in allowed_ingredients):
        return (f"({ingredients} - VALID)")
    else:
        return (f"({ingredients} - INVALID)")

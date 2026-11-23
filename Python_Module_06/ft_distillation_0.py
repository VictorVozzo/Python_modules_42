# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_distillation_0.py                               :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/22 14:49:09 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/22 14:49:10 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

from alchemy.potions import healing_potion, strength_potion


if __name__ == "__main__":
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {strength_potion()}")
    print(f"Testing healing potion: {healing_potion()}")

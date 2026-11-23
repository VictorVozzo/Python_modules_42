# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_distillation_1.py                               :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/22 15:27:10 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/22 15:27:11 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import alchemy


if __name__ == "__main__":
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    print(f"Testing heal alias: {alchemy.heal()}")

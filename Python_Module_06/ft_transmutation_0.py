# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_transmutation_0.py                              :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/24 12:47:42 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/24 12:47:42 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import alchemy.transmutation.recipes

if __name__ == "__main__":
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(
        "Testing lead to gold: "
        f"{alchemy.transmutation.recipes.lead_to_gold()}")

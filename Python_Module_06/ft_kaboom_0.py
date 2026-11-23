# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_kaboom_0.py                                     :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/24 17:02:50 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/24 17:02:50 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import alchemy.grimoire

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print("Testing record light spell:", alchemy.grimoire.light_spell_record(
        "Fantasy", "Earth, wind and fire"))

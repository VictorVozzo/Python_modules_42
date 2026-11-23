# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_alembic_2.py                                    :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/22 11:46:23 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/22 11:46:24 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import alchemy.elements


if __name__ == "__main__":
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print("Testing create_earth: ", end="")
    print(alchemy.elements.create_earth())

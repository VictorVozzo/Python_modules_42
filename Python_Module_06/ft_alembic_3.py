# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_alembic_3.py                                    :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/22 11:51:23 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/22 11:51:24 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

from alchemy.elements import create_air


if __name__ == "__main__":
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py"
          " using 'from ... import ...' structure")
    print("Testing create_air: ", end="")
    print(create_air())

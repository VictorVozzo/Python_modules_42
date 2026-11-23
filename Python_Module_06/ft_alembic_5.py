# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_alembic_5.py                                    :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/22 12:41:27 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/22 12:41:28 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

from alchemy import create_air


if __name__ == "__main__":
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print("Testing create_air: ", end="")
    print(create_air())

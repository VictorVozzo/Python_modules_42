# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_alembic_4.py                                    :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/22 11:53:26 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/22 11:53:27 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import alchemy


if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air: ", end="")
    print(alchemy.create_air())
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth: ", end="")
    print(alchemy.create_earth())

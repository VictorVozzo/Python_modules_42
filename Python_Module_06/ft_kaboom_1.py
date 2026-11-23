# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_kaboom_1.py                                     :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/24 17:29:12 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/24 17:29:12 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #


if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    import alchemy.grimoire.dark_spellbook
    print("Testing record dark spell:",
          alchemy.grimoire.dark_spellbook.dark_spell_record(
              "Avada Kedavra", "Bats, frogs and mouse tail"))
